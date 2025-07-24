from playwright.sync_api import sync_playwright


class BrowserManager:
    """Zarządza przeglądarką."""

    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def close_browser(self):
        self.context.close()
        self.browser.close()
        self.playwright.stop()


class IDreamLoginPage:
    """Reprezentuje stronę logowania idream.pl."""

    def __init__(self, page):
        self.page = page
        self.page.set_viewport_size({"width": 1920, "height": 1080})
        self.url = "https://idream.pl/logowanie.html"  # Adres strony logowania

    def open_page(self):
        self.page.goto(self.url)

    def email_input(self):
        return self.page.locator("#login_main_login")  # Lokator pola e-mail

    def password_input(self):
        return self.page.locator("#psw_main_login")  # Lokator pola hasła

    def login_button(self):
        return self.page.locator("form[name='main_login_form'] div[class='buttons-container clearfix'] button[name='dispatch[auth.login]']")  # Lokator przycisku logowania

    def login(self, email, password):
        self.email_input().fill(email)
        self.password_input().fill(password)
        self.login_button().click()