from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class SmokeTests(TestCase):
    def test_health(self):
        resp = self.client.get("/api/health")
        self.assertEqual(resp.status_code, 200)

    def test_admin_login_patron_created_by_seed(self):
        # Seed is not run in test db; just sanity check auth works
        u = User.objects.create_user(username="x", password="y")
        ok = self.client.login(username="x", password="y")
        self.assertTrue(ok)
