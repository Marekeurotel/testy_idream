class IDreamProductPage:
    def __init__(self, page):
        self.page = page

    def price(self):
        return self.page.locator(".ty-price-num").first

    def description(self):
        return self.page.locator(".idr-accordion-title").first

    def specification(self):
        return self.page.locator(".ty-tabs__a").first