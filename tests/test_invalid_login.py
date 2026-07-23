from pages.login_page import LoginPage

def test_invalid_username(browser_page):
    
    login_page = LoginPage(browser_page)

    login_page.open()

    login_page.login(
        "wrong_user",
        "secret_sauce"
    )

    assert (
        "Username and password do not match"
        in login_page.get_error_message()
    )

