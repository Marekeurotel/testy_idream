import unittest
from browser_manager import BrowserManager
from idream_main_page import IDreamHomePage


class TestSecurity(unittest.TestCase):

    def setUp(self):
        """Konfiguracja przeglądarki"""
        self.browser = BrowserManager()
        self.home_page = IDreamHomePage(self.browser.page)

    def test_sql_injection(self):
        """Test podatności na SQL Injection"""
        self.home_page.open_page()
        sql_payloads = [
            "' OR '1'='1",
            "1; DROP TABLE users;",
            "' UNION SELECT 1,2,3 --"
        ]

        for payload in sql_payloads:
            with self.subTest(payload=payload):
                search_box = self.home_page.search_input()
                search_box.fill("")
                search_box.fill(payload)
                search_box.press("Enter")
                self.browser.page.wait_for_timeout(2000)
                page_source = self.browser.page.content()
                self.assertNotIn("You have an error in your SQL syntax", page_source,
                                 f"Strona podatna na SQL Injection przy payload: {payload}")

    def test_xss_attack(self):
        """Test podatności na XSS (Cross-Site Scripting)"""
        self.home_page.open_page()
        xss_payloads = [
            "<script>alert('XSS')</script>",
            '\"><script>alert("XSS")</script>',
            "<img src=x onerror=alert('XSS')>"
        ]

        for payload in xss_payloads:
            with self.subTest(payload=payload):
                search_box = self.home_page.search_input()
                search_box.fill("")
                search_box.fill(payload)
                search_box.press("Enter")
                self.browser.page.wait_for_timeout(2000)
                page_source = self.browser.page.content()
                self.assertNotIn(payload, page_source, "Strona podatna na XSS!")
    def tearDown(self):
        """Zamykanie przeglądarki"""
        self.browser.close_browser()
