import os
import pytest
from datetime import datetime
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser_page():

    headless = os.getenv("HEADLESS", "false").lower() == "true"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless
        )

        page = browser.new_page()

        yield page

        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("browser_page")

        if page:

            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshot_path = (
                f"screenshots/{item.name}_{timestamp}.png"
            )

            page.screenshot(path=screenshot_path)

            print(
                f"\nScreenshot saved: {screenshot_path}"
            )