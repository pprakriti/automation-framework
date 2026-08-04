from utils.logger import get_logger


class CartPage:

    logger = get_logger()

    def __init__(self, page):
        self.page = page

        self.cart_title = ".title"
        self.product_name = ".inventory_item_name"
        self.checkout_button = "#checkout"


    def is_loaded(self):

        self.logger.info(
            "Checking if cart page is loaded"
        )

        title = self.page.locator(
            self.cart_title
        ).inner_text()

        if title == "Your Cart":

            self.logger.info(
                "Cart page loaded successfully"
            )

            return True

        else:

            self.logger.error(
                f"Unexpected cart title: {title}"
            )

            return False


    def get_product_name(self):

        self.logger.info(
            "Getting product name from cart"
        )

        return self.page.locator(
            self.product_name
        ).inner_text()

    def click_checkout(self):

        self.logger.info(
            "Clicking checkout button"
        )

        self.page.locator(
            self.checkout_button
        ).click()
