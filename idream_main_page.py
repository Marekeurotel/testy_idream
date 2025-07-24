from playwright.sync_api import Page, expect

class IDreamHomePage:
    """Reprezentuje stronę główną idream.pl."""

    def __init__(self, page):
        self.page = page
        self.page.set_viewport_size({"width": 1920, "height": 1080})
        self.url = "https://www.idream.pl/"  # Adres strony głównej

        # --- Lokatory dla strony głównej ---
        # Zakładamy, że przyciski mediów społecznościowych są w stopce
        self.instagram_button_locator = self.page.locator("a[href*='instagram.com/idream_pl']")
        self.facebook_button_locator = self.page.locator("a[href*='facebook.com/iDreamPolska']")
        self.tiktok_button_locator = self.page.locator("a[href*='tiktok.com/@idream_pl']")
        self.youtube_button_locator = self.page.locator("//a[@href='https://www.youtube.com/user/iDreamPL/']")
        self.first_product_card_locator = self.page.locator("(//div[contains(@class,'ut2-gl__body')])[1]")
        self.add_to_wishlist_button_selector = ".ut2-add-to-wish.cm-submit.cm-tooltip"
        self.wishlist_count_icon_locator = self.page.locator(".ut2-top-wishlist-count")

        # Lokator dla przycisku akceptacji cookies
        self.cookie_consent_button = self.page.get_by_role("button", name="W porządku")

    def open_page(self):
        """Otwiera stronę główną."""
        self.page.goto(self.url)
        self.handle_cookie_consent()

    def handle_cookie_consent(self):
        """Obsługuje wyskakujące okno z cookies."""
        try:
            # Czekamy na pojawienie się przycisku akceptacji cookies
            cookie_button = self.page.locator("#garua_cookie_consent_popup_button_allow")
            if cookie_button.is_visible(timeout=5000):  # Czekamy max 5 sekund
                cookie_button.click()
                self.page.wait_for_timeout(1000)  # Czekamy na zamknięcie okna
        except:
            # Jeśli nie znaleziono przycisku lub wystąpił inny błąd, kontynuujemy
            pass

    def add_first_product_to_wishlist(self):
        """
        Dodaje pierwszy produkt z listy do listy życzeń.
        Obsługuje najechanie i kliknięcie przycisku.
        """
        # Czekamy, aż KARTA PRODUKTU będzie widoczna, zanim na nią najedziemy
        expect(self.first_product_card_locator).to_be_visible(timeout=15000)  # Zwiększony timeout

        # Znajdź przycisk WEWNĄTRZ pierwszej karty produktu
        add_button = self.first_product_card_locator.locator(self.add_to_wishlist_button_selector)

        self.first_product_card_locator.hover()  # Najedź na kartę produktu

        # Czekaj na widoczność przycisku po najechaniu
        expect(add_button).to_be_visible(timeout=5000)

        add_button.click()

    def scroll_to_bottom(self):
        """Przewija stronę na sam dół, aby upewnić się, że stopka jest widoczna."""
        self.page.mouse.wheel(0, 10000)  # Przewijamy o dużą wartość w dół

    def get_title(self):
        """Zwraca tytuł strony."""
        return self.page.title()

    def search_input(self):
        return self.page.locator("input#search_input")

    def click_social_media_button(self, button_type: str) -> Page:
        """
        Klika w przycisk mediów społecznościowych i zwraca obiekt Page dla nowego okna/karty.
        :param button_type: Typ przycisku ('instagram', 'facebook', 'tiktok', 'youtube').
        :return: Obiekt Page reprezentujący nowo otwartą kartę/okno.
        """
        button_locator = None
        if button_type == 'instagram':
            button_locator = self.instagram_button_locator
        elif button_type == 'facebook':
            button_locator = self.facebook_button_locator
        elif button_type == 'tiktok':
            button_locator = self.tiktok_button_locator
        elif button_type == 'youtube':
            button_locator = self.youtube_button_locator
        else:
            raise ValueError(f"Nieznany typ przycisku mediów społecznościowych: {button_type}")

        expect(button_locator).to_be_visible(timeout=10000)

        with self.page.expect_popup() as popup_info:
            button_locator.click()

        popup_page = popup_info.value
        # Poczekaj na załadowanie stanu sieci dla popupu
        popup_page.wait_for_load_state('load', timeout=15000)
        return popup_page

    def get_social_media_expected_url(self, button_type: str) -> str:
        """Zwraca oczekiwany URL dla danego przycisku mediów społecznościowych."""
        if button_type == 'instagram':
            return "https://www.instagram.com/idream_pl/"
        elif button_type == 'facebook':
            return "https://www.facebook.com/iDreamPolska/"
        elif button_type == 'tiktok':
            return "https://www.tiktok.com/@idream_pl"
        elif button_type == 'youtube':
            return "https://www.youtube.com/@idream_pl"  # Zaktualizowany URL, aby był bardziej bezpośredni
        else:
            raise ValueError(f"Nieznany typ przycisku mediów społecznościowych: {button_type}")

    def cart_content_button(self):
        return self.page.locator("div.ut2-top-cart-content")

    def my_account_button(self):
        return self.page.locator("div.ut2-top-my-account")

    def wishlist_button(self):
        return self.page.locator("a.cm-tooltip.ty-wishlist__a")

    def compared_products_button(self):
        return self.page.locator("#abt__ut2_compared_products")

    def add_to_wish_button(self):
        return self.page.locator(".ut2-add-to-wish.cm-submit.cm-tooltip")


class IDreamProductPage:
    def __init__(self, page):
        self.page = page

    def product_cart(self):
        self.page.locator("button:has-text('Do koszyka')").first.click()
        self.page.wait_for_timeout(2000)  # Wait for 2 seconds
        self.page.locator("a.ty-btn.ty-btn__secondary.cm-notification-close:has-text('Kontynuuj zakupy')").first.click()
        self.page.wait_for_timeout(1000)  # Wait for 1 second


if __name__ == "__main__":
    browser = None

    # Uruchomienie przeglądarki i wejście na stronę główną
    try:
        browser = BrowserManager()
        home_page = IDreamHomePage(browser.page)
        home_page.page.browser_manager = browser  # Dodajemy referencję do browser_manager

        # Otwórz stronę główną
        home_page.open_page()
        browser.page.wait_for_timeout(2000)  # Wait for 2 seconds

        # Pobierz tytuł strony i wyświetl go w konsoli
        print(f"Tytuł strony: {home_page.get_title()}")
    finally:
        # Zawsze zamykaj przeglądarkę, nawet w przypadku błędów
        if browser:
            browser.close_browser()
