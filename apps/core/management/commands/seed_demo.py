from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.core.models import Company

User = get_user_model()

DEMO_USERS = [
    ("patron", True, True),
    ("satinalma", False, False),
    ("pm", False, False),
    ("santiye", False, False),
    ("finans", False, False),
]

class Command(BaseCommand):
    help = "Create demo company and demo users (idempotent)."

    def handle(self, *args, **options):
        company, _ = Company.objects.get_or_create(
            name="TNT Mühendislik (Demo)",
            defaults={"tax_no": "0000000000", "trade_registry_no": "DEMO-TR"},
        )
        for username, is_staff, is_superuser in DEMO_USERS:
            user, created = User.objects.get_or_create(username=username)
            user.is_staff = is_staff or is_superuser
            user.is_superuser = is_superuser
            user.set_password("demo1234")
            user.save()
            # attach company + default language
            if hasattr(user, "profile"):
                user.profile.company = company
                user.profile.preferred_language = "tr"
                user.profile.save()

        self.stdout.write(self.style.SUCCESS("Demo seed OK"))
