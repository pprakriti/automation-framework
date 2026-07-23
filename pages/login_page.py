class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username = "#user-name"
        self.password = "#password"
        self.login_button= "#login-button"
        self.error_message = "[data-test='error']"

    def open(self):
        self.page.goto(
            "https://www.saucedemo.com"
        )

    def login(self, username, password):

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
    
    def get_error_message(self):
        return self.page.locator(
            self.error_message
        ).inner_text()
