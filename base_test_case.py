import unittest
from browser_manager import BrowserManager
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext

class BrowserTestCase(unittest.TestCase):

    playwright: sync_playwright
    browser: Browser
    context: BrowserContext
    page: Page

    def setUp(self):
        self.browser_manager = BrowserManager(headless=False)  # True dla uruchamiania bez GUI
        self.page = self.browser_manager.page
        self.browser = self.browser_manager.browser


    def tearDown(self):
        """Zamyka przeglądarkę Playwright po każdym teście."""
        self.browser_manager.close_browser()