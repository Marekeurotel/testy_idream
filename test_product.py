from base_test_case import BrowserTestCase
from idream_main_page import IDreamHomePage, IDreamProductPage



class TestIDreamAddToCart(BrowserTestCase):

    def setUp(self):
        super().setUp()
        self.home_page = IDreamHomePage(self.page)
        self.home_page.page.browser_manager = self.browser
        self.product_page = IDreamProductPage(self.page)

    def test_add_product_to_cart(self):
        self.home_page.open_page()
        self.product_page.product_cart()
        self.page.wait_for_timeout(2000)  # Wait for 2 seconds

        # Sprawdź, czy produkt został dodany (np. sprawdzając obecność koszyka)
        # Sprawdzamy, czy w koszyku jest co najmniej 1 produkt
        cart_element = self.page.locator(".ty-minicart-count")
        cart_count = cart_element.text_content()
        self.assertGreater(int(cart_count), 0, "Produkt został dodany do koszyka.")
        print(f"Produkty w koszyku: {cart_count}")

    def tearDown(self):
        """Sprzątanie po teście: zamknięcie przeglądarki."""
        self.browser_manager.close_browser()

