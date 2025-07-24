from base_test_case import BrowserTestCase
from idream_login_page import *


class TestIDreamLogin(BrowserTestCase):

    def setUp(self):
        super().setUp()
        self.login_page = IDreamLoginPage(self.page)

    def test_login(self):
        self.login_page.open_page()
        try:
            # Wait for and click the cookie consent button
            self.page.wait_for_selector("#garua_cookie_consent_popup_button_allow", timeout=5000)
            self.page.click("#garua_cookie_consent_popup_button_allow")
        except Exception as e:
            print("Okienko cookies nie zostało znalezione lub nie można go kliknąć:", e)
        
        self.login_page.login("mszylejko2@eurotel.pl", "rickandmorty")
        self.page.wait_for_timeout(2000)  # Wait for 2 seconds

        # Check if login was successful
        page_content = self.page.content()
        self.assertIn("Użytkownik został poprawnie zalogowany", page_content, "Logowanie nie powiodło się.")

    def tearDown(self):
        """Sprzątanie po teście: zamknięcie przeglądarki."""
        self.browser_manager.close_browser()