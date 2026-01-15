from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.core.api import HealthView, MeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/health", HealthView.as_view(), name="health"),
    path("api/me", MeView.as_view(), name="me"),
]
