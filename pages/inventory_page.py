class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.title = ".title"

    def is_loaded(self):
        return self.page.locator(self.title).inner_text() == "Products"