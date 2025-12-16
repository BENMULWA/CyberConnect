from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

# -----------------------------
# Service Model
# -----------------------------
class Service(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            counter = 1
            while Service.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    @property
    def image_url(self):
        from django.templatetags.static import static
        return static(self.image)

    @property
    def formatted_price(self):
        return f"KSh {self.price:,.2f}"


# -----------------------------
# Order Model (Booking & Checkout)
# -----------------------------
class Order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    till_no = models.CharField(max_length=20, blank=True, null=True)
    transaction_code = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Auto-generate Till No if blank
        if not self.till_no:
            self.till_no = "3655623"  # fixed till number
        # Auto-generate transaction code if blank
        if not self.transaction_code:
            import uuid
            self.transaction_code = f"TILL{str(uuid.uuid4().int)[:8]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.service.name if self.service else 'General'} (Total: KSh {self.total}, Till: {self.till_no})"
