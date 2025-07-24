from playwright.sync_api import sync_playwright

class BrowserManager:
    """Zarządza przeglądarką."""

    def __init__(self, headless=False):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def close_browser(self):
        """Zamyka przeglądarkę."""
        self.context.close()
        self.browser.close()
        self.playwright.stop() 