import os
from dotenv import load_dotenv

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

load_dotenv()


def test_successful_login(browser_page):

    login_page = LoginPage(browser_page)
    inventory_page = InventoryPage(browser_page)

    login_page.open()

    login_page.login(
       os.getenv("SAUCE_USERNAME"),
       os.getenv("SAUCE_PASSWORD")
    )

    assert inventory_page.is_loaded()