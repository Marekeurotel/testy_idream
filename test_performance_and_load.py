import unittest
from base_test_case import BrowserTestCase
from idream_main_page import IDreamHomePage
import time

class TestPerformanceAndLoad(BrowserTestCase):
    def setUp(self):
        super().setUp()
        self.home_page = IDreamHomePage(self.page)

    def test_page_load_time(self):
        start_time = time.time()
        self.home_page.open_page()
        self.page.wait_for_load_state("load")
        load_time = time.time() - start_time
        self.assertLess(load_time, 5, f"Strona ładowała się zbyt długo: {load_time:.2f} sekundy")

    def test_multiple_users(self):
        # Przykładowy test symulujący wielu użytkowników
        for _ in range(5):
            self.home_page.open_page()
            self.page.wait_for_timeout(500)

if __name__ == "__main__":
    unittest.main()
