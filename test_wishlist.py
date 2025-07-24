
from base_test_case import BrowserTestCase
from idream_main_page import IDreamHomePage
from playwright.sync_api import expect

class TestWishlist(BrowserTestCase):

    def setUp(self):
        """Przygotowanie do testu: uruchomienie przeglądarki i wejście na stronę."""
        super().setUp()
        self.home_page = IDreamHomePage(self.page)

    def test_wishlist_button(self):
        self.home_page.open_page()
        self.home_page.add_first_product_to_wishlist()
        expect(self.home_page.wishlist_count_icon_locator).to_have_text("1", timeout=10000)
        expect(self.home_page.wishlist_count_icon_locator).to_be_visible(timeout=5000)
        current_count = self.home_page.wishlist_count_icon_locator.text_content()
        print(f"Liczba produktów na liście życzeń: {current_count}")

    def tearDown(self):
        """Zamyka przeglądarkę Playwright po każdym teście."""
        super().tearDown()


