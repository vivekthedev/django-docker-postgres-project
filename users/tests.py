from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="vivekks", email="contact@vivek.com", password="pass12345"
        )

        self.assertEqual(user.username, "vivekks")
        self.assertEqual(user.email, "contact@vivek.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="supervivek", email="contact@super.com", password="pass12345"
        )
        self.assertEqual(admin_user.username, "supervivek")
        self.assertEqual(admin_user.email, "contact@super.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
