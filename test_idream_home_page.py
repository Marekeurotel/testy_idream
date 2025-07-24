from base_test_case import BrowserTestCase
from idream_main_page import IDreamHomePage


class TestIDreamHomePage(BrowserTestCase):

    def test_open_home_page(self):
        """Test sprawdzający, czy strona główna się otwiera."""
        home_page = IDreamHomePage(self.page)
        home_page.open_page()
        self.assertIn("iDream", home_page.get_title(), "Strona główna nie otworzyła się poprawnie!")