from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

class Service(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # store the image filename (e.g. "services/birth_certificate.png")
    image = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # automatically generate slug if not provided
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
        """Return the static image path for this service."""
        from django.templatetags.static import static
        return static(self.image)

    @property
    def formatted_price(self):
        return f"KSh {self.price:,.2f}"


class ServiceBooking(models.Model):
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    transaction_code = models.CharField(max_length=128, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='bookings')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.full_name} — {self.service.name} ({self.created_at:%Y-%m-%d %H:%M})"
    

    #the models that handles the checkout orders after client fills the required details
    from django.db import models

class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - KSh {self.total}"

