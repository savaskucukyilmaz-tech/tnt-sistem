from django.contrib import admin
from .models import Company, UserProfile

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "tax_no", "trade_registry_no", "created_at")
    search_fields = ("name", "tax_no", "trade_registry_no")

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "company", "preferred_language")
    search_fields = ("user__username",)
