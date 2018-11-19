from django.test import TestCase


class TestViews(TestCase):
    def test_get_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_get_registration_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
        
    def test_get_logout_page(self):
        page = self.client.get("/accounts/logout/")
        self.assertEqual(page.status_code, 302)