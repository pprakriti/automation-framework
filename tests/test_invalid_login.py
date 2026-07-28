import pytest

from pages.login_page import LoginPage
from utils.data_reader import load_login_data


@pytest.mark.parametrize(
    "username,password,expected_error",
    load_login_data()
)
def test_invalid_login(browser_page, username, password, expected_error):

    login_page = LoginPage(browser_page)

    login_page.open()

    login_page.login(
        username,
        password
    )

    assert (
        expected_error
        in login_page.get_error_message()
    )