from base_test_case import BrowserTestCase
from idream_main_page import IDreamHomePage

class TestSearchBar(BrowserTestCase):
    def setUp(self):
        super().setUp()
        self.home_page = IDreamHomePage(self.page)

    def test_search_bar(self):
        self.home_page.open_page()
        search_input = self.home_page.search_input()
        search_input.fill("iPhone")
        search_input.press("Enter")
        self.page.wait_for_timeout(2000)
        results = self.page.locator(".ty-mainbox-title__right").all()
        self.assertGreater(len(results), 0, "Brak wyników wyszukiwania!")