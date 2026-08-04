import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_add_product_to_cart(browser_page):

    login_page = LoginPage(browser_page)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    inventory_page = InventoryPage(
        browser_page
    )

    assert inventory_page.is_loaded()

    inventory_page.add_product_to_cart()

    assert inventory_page.get_cart_count() == "1"
