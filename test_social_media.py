from base_test_case import BrowserTestCase
from idream_main_page import IDreamHomePage
from playwright.sync_api import Page, expect


class TestSocialMediaButtons(BrowserTestCase):
    def setUp(self):
        super().setUp()
        self.home_page = IDreamHomePage(self.page)

    def _run_social_media_test(self, button_type: str, expected_url_start: str = None):
        """
        Pomocnicza metoda do uruchamiania testów przycisków mediów społecznościowych.
        """
        self.home_page.open_page()
        ## self.home_page.scroll_to_bottom()  # Przewijamy, by przyciski były widoczne

        popup_page: Page = self.home_page.click_social_media_button(button_type)

        # Pobieramy bieżący URL z popupu
        current_url = popup_page.url
        print(f"Otwarty URL dla {button_type}: {current_url}")

        # Pobieramy oczekiwany URL z Page Objectu
        expected_url = self.home_page.get_social_media_expected_url(button_type)

        if expected_url_start:
            # Dla YouTube, gdzie URL może być dynamiczny, sprawdzamy początek
            self.assertTrue(current_url.startswith(expected_url_start),
                            f"Odnośnik do {button_type} jest niepoprawny. Oczekiwano startu z '{expected_url_start}', otrzymano '{current_url}'.")
        else:
            # Dla innych, sprawdzamy dokładny URL
            self.assertEqual(current_url, expected_url,
                             f"Odnośnik do {button_type} jest niepoprawny. Oczekiwano '{expected_url}', otrzymano '{current_url}'.")

        popup_page.close()

    def test_instagram_link(self):
        self._run_social_media_test('instagram')

    def test_facebook_link(self):
        self._run_social_media_test('facebook')

    def test_tiktok_link(self):
        self._run_social_media_test('tiktok')

    def test_youtube_link(self):
        # Dla YouTube nadal musisz podać oczekiwany startowy URL, jeśli jest dynamiczny
        # Najlepiej, aby Page Object dostarczał sensowny URL bazowy.
        # W nowej wersji Page Objectu próbujemy celować w bezpośredni URL kanału YouTube.
        self._run_social_media_test('youtube', expected_url_start="https://consent.youtube.com/m?continue=https%3A%2F%2Fwww.youtube.com%2Fuser%2FiDreamPL%3Fcbrd%3D1&gl=PL&m=0&pc=yt&cm=2&hl=pl&src=1")
        # Jeśli nadal przekierowuje przez googleusercontent, możesz rozważyć:
        # 1. Zmianę selektora przycisku YouTube, aby prowadził bezpośrednio.
        # 2. Akceptację, że to przekierowanie jest normalne i sprawdzenie, czy końcowy URL jest poprawny
        #    po serii przekierowań (co jest trudniejsze bez głębokiej inspekcji sieci).
        # Na razie trzymam się prostszego sprawdzenia `startswith`, ale z nowym URL bazowym.
