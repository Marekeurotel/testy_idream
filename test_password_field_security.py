import unittest
from base_test_case import BrowserTestCase
from idream_login_page import *


class TestSecurity(BrowserTestCase):

    def setUp(self):
        super().setUp()
        self.login_page = IDreamLoginPage(self.page)
        self.page.goto("https://idream.pl/logowanie.html")

    def test_password_field_security(self):
        """Test sprawdzający, czy pole hasła jest ukryte"""
        try:
            password_field = self.page.locator("#psw_main_login")
            field_type = password_field.get_attribute("type")

            self.assertEqual(field_type, "password", "Pole hasła nie jest ukryte!")
        except Exception as e:
            self.fail(f"Test nie powiódł się: {str(e)}")