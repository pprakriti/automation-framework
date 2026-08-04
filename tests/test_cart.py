from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_verify_product_in_cart(browser_page):

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

    inventory_page.open_cart()


    cart_page = CartPage(
        browser_page
    )

    assert cart_page.is_loaded()

    assert (
        cart_page.get_product_name()
        == "Sauce Labs Backpack"
    )
