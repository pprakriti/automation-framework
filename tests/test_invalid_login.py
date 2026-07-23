from pages.login_page import LoginPage
from utils.data_reader import load_test_data

def test_invalid_username(browser_page):
    
    login_page = LoginPage(browser_page)

    login_page.open()

    data = load_test_data()

    login_page.login(

       data["invalid_user"]["username"],
       data["invalid_user"]["password"]
    )

    assert (
        "Username and password do not match"
        in login_page.get_error_message()
    )

