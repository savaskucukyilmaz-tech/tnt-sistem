from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Company(models.Model):
    name = models.CharField(max_length=200)
    tax_no = models.CharField(max_length=20)  # required for real usage
    trade_registry_no = models.CharField(max_length=50, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    preferred_language = models.CharField(max_length=5, choices=settings.LANGUAGES, default="tr")

    def __str__(self) -> str:
        return f"{self.user.username} profile"
