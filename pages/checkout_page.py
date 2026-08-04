from utils.logger import get_logger


class CheckoutPage:

    logger = get_logger()

    def __init__(self, page):
        self.page = page

        self.checkout_button = "#checkout"

        self.first_name = "#first-name"
        self.last_name = "#last-name"
        self.postal_code = "#postal-code"

        self.continue_button = "#continue"

        self.finish_button = "#finish"

        self.confirmation_message = ".complete-header"


    def click_checkout(self):

        self.logger.info(
            "Clicking checkout button"
        )

        self.page.locator(
            self.checkout_button
        ).click()


    def enter_customer_information(
        self,
        first_name,
        last_name,
        postal_code
    ):

        self.logger.info(
            "Entering customer information"
        )

        self.page.locator(
            self.first_name
        ).fill(first_name)

        self.page.locator(
            self.last_name
        ).fill(last_name)

        self.page.locator(
            self.postal_code
        ).fill(postal_code)


    def continue_checkout(self):

        self.logger.info(
            "Continuing checkout"
        )

        self.page.locator(
            self.continue_button
        ).click()


    def finish_order(self):

        self.logger.info(
            "Finishing order"
        )

        self.page.locator(
            self.finish_button
        ).click()


    def get_confirmation_message(self):

        self.logger.info(
            "Getting order confirmation message"
        )

        return self.page.locator(
            self.confirmation_message
        ).inner_text()
