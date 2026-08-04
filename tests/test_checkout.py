import os
from dotenv import load_dotenv

from utils.data_reader import get_customer

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


load_dotenv()


def test_complete_checkout(browser_page):

    login_page = LoginPage(browser_page)

    login_page.open()

    login_page.login(
        os.getenv("SAUCE_USERNAME"),
        os.getenv("SAUCE_PASSWORD")
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

    cart_page.click_checkout()


    checkout_page = CheckoutPage(
        browser_page
    )

    customer = get_customer()

    checkout_page.enter_customer_information(
        customer["first_name"],
        customer["last_name"],
        customer["postal_code"]
    )

    checkout_page.continue_checkout()

    checkout_page.finish_order()


    assert (
        checkout_page.get_confirmation_message()
        == "Thank you for your order!"
    )
