from django.contrib import admin
from .models import Service, Order

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "price", "slug")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "service",
        "phone",
        "total",
        "till_no",
        "transaction_code",
        "created_at",
    )
    list_filter = ("service", "created_at")
    search_fields = ("first_name", "last_name", "phone", "transaction_code", "till_no")
