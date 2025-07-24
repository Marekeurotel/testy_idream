from base_test_case import BrowserTestCase
from idream_main_page import IDreamHomePage
import requests


class TestMainMenuNavigation(BrowserTestCase):

    def setUp(self):
        super().setUp()
        self.home_page = IDreamHomePage(self.page)
        self.home_page.page.browser_manager = self.browser

    def test_main_menu_links(self):
        self.home_page.open_page()
        self.page.wait_for_timeout(1000)  # Wait for 1 second

        # Znajdź menu główne
        main_menu = self.page.locator("#sw_dropdown_541")
        menu_links = main_menu.locator("a").all()  # Pobierz wszystkie linki w menu

        for link in menu_links:
            link_text = link.text_content()
            href = link.get_attribute("href")

            with self.subTest(link=link_text):
                print(f"Sprawdzam link: {link_text} -> {href}")

                # Sprawdź, czy href nie jest pusty lub None
                self.assertIsNotNone(href, f"Link '{link_text}' ma pusty atrybut href.")
                self.assertNotEqual(href, "", f"Link '{link_text}' ma pusty atrybut href.")

                # Weryfikacja poprawności linku poprzez żądanie HTTP
                response = requests.get(href)
                self.assertEqual(response.status_code, 200, f"Strona {href} zwróciła status {response.status_code}.")

                # Opcjonalnie: Kliknij link i sprawdź, czy strona się załaduje
                self.page.goto(href)
                self.assertTrue(self.page.title(), f"Strona {href} nie ma tytułu.")
                self.page.go_back()