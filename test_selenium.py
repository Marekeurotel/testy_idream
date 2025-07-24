import unittest
from base_test_case import BrowserTestCase
from playwright.sync_api import sync_playwright

class TestSeleniumExample(BrowserTestCase):
    def test_google_search(self):
        self.page.goto("https://google.com/")
        self.page.goto("https://idream.pl")
        self.page.set_viewport_size({"width": 1920, "height": 1080})
        self.page.wait_for_selector("input[name='q']", timeout=1000)
        search_box = self.page.locator("input[name='q']")
        search_box.fill("słuchawki")
        search_box.press("Enter")
        self.page.wait_for_timeout(3000)

