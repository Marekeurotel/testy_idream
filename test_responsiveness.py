import unittest
from base_test_case import BrowserTestCase
from playwright.sync_api import TimeoutError
from idream_main_page import IDreamHomePage

class TestResponsiveness(BrowserTestCase):
    def setUp(self):
        super().setUp()
        self.home_page = IDreamHomePage(self.page)
        self.home_page.handle_cookie_consent()

    def handle_cookies(self):
        """Metoda do obsługi bannera cookies."""
        try:
            # Używamy selektora tekstowego, jest on często bardziej stabilny
            accept_button = self.page.locator("button:has-text('W porządku')")
            # Czekamy na przycisk maksymalnie 5 sekund (powinien pojawić się szybko)
            accept_button.wait_for(timeout=5000)
            accept_button.click()
            print("INFO: Banner cookies został zaakceptowany.")
        except TimeoutError:
            # Jeśli przycisk się nie pojawi, to znaczy, że banner już został zaakceptowany
            # lub go nie ma. To nie jest błąd.
            print("INFO: Banner cookies nie został znaleziony (prawdopodobnie już zaakceptowany).")

    def is_page_displayed_correctly(self):
        """Ulepszona metoda do sprawdzania widoczności kluczowych elementów."""
        try:
            logo_selector = ".top-logo img[alt='Logo iDream']"
            logo = self.page.locator(logo_selector).first

            # Czekamy, aż sam lokator będzie widoczny
            logo.wait_for(state='visible', timeout=8000)

            print(f"INFO: Znaleziono logo za pomocą selektora '{logo_selector}'. Element jest widoczny.")
            return True
        except TimeoutError:
            # Jeśli element nie stał się widoczny w 8s, logujemy błąd
            print(
                f"BŁĄD KRYTYCZNY: Element '{logo_selector}' nie został znaleziony lub nie stał się widoczny w wyznaczonym czasie.")
            # Zrób zrzut ekranu, aby zobaczyć, co poszło nie tak
            self.page.screenshot(path="debug_screenshot.png")
            return False

    def run_responsiveness_test(self, viewport_size, device_name):
        """Ujednolicona metoda do przeprowadzania testu responsywności."""
        self.home_page.open_page()
        self.page.set_viewport_size(viewport_size)

        # NAJWAŻNIEJSZY KROK: obsługa cookies PRZED weryfikacją
        self.handle_cookies()

        # Asercja z bardziej czytelnym komunikatem
        error_message = f"Strona nie wyświetla się poprawnie na {device_name} (rozmiar: {viewport_size['width']}x{viewport_size['height']})."
        self.assertTrue(self.is_page_displayed_correctly(), error_message)

    def test_desktop_view(self):
        """Test widoku desktopowego."""
        self.run_responsiveness_test({"width": 1920, "height": 1080}, "desktopie")

    def test_mobile_view(self):
        """Test widoku mobilnego."""
        self.run_responsiveness_test({"width": 375, "height": 812}, "mobile")

    def test_tablet_view(self):
        """Test widoku tabletowego."""
        self.run_responsiveness_test({"width": 768, "height": 1024}, "tablecie")