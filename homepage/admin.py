from django.contrib import admin
from .models import Service, ServiceBooking

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "price", "slug")

@admin.register(ServiceBooking)
class ServiceBookingAdmin(admin.ModelAdmin):
    list_display = ("full_name", "service", "phone_number", "transaction_code", "created_at")
    list_filter = ("service", "created_at")
