from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_successful_login(browser_page):

    login_page = LoginPage(browser_page)
    inventory_page = InventoryPage(browser_page)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert browser_page.url == (
        "https://www.saucedemo.com/inventory.html"
    )

    assert inventory_page.is_loaded()