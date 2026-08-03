from pages.base_page import BasePage
from utils.logger import get_logger


class LoginPage(BasePage):

    logger = get_logger()

    def __init__(self, page):
        super().__init__(page)

        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"


    def open(self):
        self.logger.info("Opening SauceDemo login page")
        self.page.goto("https://www.saucedemo.com/")


    def login(self, username, password):

        self.logger.info(
            f"Attempting login with username: {username}"
        )

        self.page.fill(
            self.username,
            username
        )

        self.page.fill(
            self.password,
            password
        )

        self.page.click(
            self.login_button
        )

        self.logger.info("Clicked login button")


    def get_error_message(self):

        self.logger.info("Fetching login error message")

        return self.page.locator(
            self.error_message
        ).inner_text()