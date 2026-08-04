from utils.logger import get_logger


class InventoryPage:

    logger = get_logger()

    def __init__(self, page):
        self.page = page
        self.title = ".title"
        self.add_to_cart_button = "#add-to-cart-sauce-labs-backpack"
        self.cart_badge = ".shopping_cart_badge"


    def is_loaded(self):

        self.logger.info(
            "Checking if inventory page is loaded"
        )

        page_title = self.page.locator(
            self.title
        ).inner_text()

        if page_title == "Products":

            self.logger.info(
                "Inventory page loaded successfully"
            )

            return True

        else:

            self.logger.error(
                f"Unexpected inventory page title: {page_title}"
            )

            return False
    def add_product_to_cart(self):

        self.logger.info(
            "Adding Sauce Labs Backpack to cart"
        )

        self.page.locator(
            self.add_to_cart_button
        ).click()


    def get_cart_count(self):

        self.logger.info(
            "Getting cart item count"
        )

        return self.page.locator(
            self.cart_badge
        ).inner_text()