class HomePage:
    def __init__(self, page):
        self.page = page

    def open(self, url="https://example.com"):
        self.page.goto(url, wait_until="domcontentloaded")

    def load_fixture(self, html: str):
        self.page.set_content(html)

    def heading(self):
        return self.page.locator("h1").inner_text()
