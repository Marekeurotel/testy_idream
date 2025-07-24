from base_test_case import BrowserTestCase
from idream_main_page import IDreamHomePage



class TestProductDetails(BrowserTestCase):

    def setUp(self):
        super().setUp()
        self.home_page = IDreamHomePage(self.page)
        self.home_page.page.browser_manager = self.browser
        self.product_page_url = "https://idream.pl/ipad/apple-ipad-11-wi-fi-128gb-11-gen-niebieski.html"
        self.page.goto(self.product_page_url)
        self.page.wait_for_load_state("networkidle")

    def test_product_details_displayed(self):
        """Sprawdzenie, czy szczegóły produktu są wyświetlane poprawnie."""
        # Znajdź elementy ze szczegółami produktu.
        price_element = self.page.locator(".ty-price").first
        description_element = self.page.locator(".idr-accordion-title", has_text="Skrócony opis")
        specification_element = self.page.locator(".ty-tabs__a", has_text="Dane techniczne")

        # Sprawdzenie, czy elementy są widoczne
        self.assertTrue(price_element.is_visible(), "Cena produktu nie jest wyświetlana.")
        self.assertTrue(description_element.is_visible(), "Opis produktu nie jest wyświetlany.")
        self.assertTrue(specification_element.is_visible(), "Specyfikacja produktu nie jest wyświetlana.")

        # Sprawdzenie, czy tekst w elementach nie jest pusty
        self.assertNotEqual(price_element.text_content().strip(), "", "Cena produktu jest pusta.")
        self.assertNotEqual(description_element.text_content().strip(), "", "Opis produktu jest pusty.")
        self.assertNotEqual(specification_element.text_content().strip(), "", "Specyfikacja produktu jest pusta.")