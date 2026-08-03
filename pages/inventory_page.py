from utils.logger import get_logger


class InventoryPage:

    logger = get_logger()

    def __init__(self, page):
        self.page = page
        self.title = ".title"


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