# Automation Framework - Playwright + Pytest

A web automation testing framework built using:
**Python, Playwright, and Pytest** following the **Page Object Model (POM)** design pattern.

This project demonstrates SDET practices including UI automation, reusable page objects, test data management, environment-based credential handling, cross-browser testing, and automated CI/CD execution.

---

## Tech Stack

- **Programming Language:** Python 3.12
- **Automation Tool:** Playwright
- **Testing Framework:** Pytest
- **Browser Automation:** Chromium, Firefox, WebKit
- **Test Design Pattern:** Page Object Model (POM)
- **Test Data Management:** JSON
- **Environment Management:** python-dotenv
- **Reporting:** pytest-html
- **Version Control:** Git & GitHub
- **CI/CD:** GitHub Actions

---

## Framework Features

- Page Object Model architecture
- Reusable Playwright fixtures
- Data-driven testing using JSON files
- Environment-based credential management
- Smoke and regression test suites
- Cross-browser testing support
- Automatic screenshot capture on failures
- HTML test reporting
- GitHub Actions CI pipeline

---

## Project Structure

```text
automation-framework/

├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_invalid_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── data/
│   └── users.json
│
├── utils/
│   ├── logger.py
│   └── data_reader.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── .github/
    └── workflows/
        └── playwright.yml
```

## Installation

Clone repository:

```bash
git clone https://github.com/pprakriti/automation-framework.git
```


## Create virtual environment:
```bash
python -m venv venv
```

## Activate environment:
```bash
source venv/bin/activate
```

## Install dependencies:
```bash
pip install -r requirements.txt
```

## Install Playwright browsers:
```bash
playwright install
```

## Running Tests

## Run complete test suite:
```bash
pytest
```

## Generate HTML report:
```bash
pytest --html=reports/test_report.html --self-contained-html
```

## Test Markers

## Run smoke tests:
```bash
pytest -m smoke
```

## Run regression tests:
```bash
pytest -m regression
```

## Cross Browser Testing

## Run Chromium:
```bash
pytest --browser chromium
```

## Run Firefox:
```bash
pytest --browser firefox
```

## Run WebKit:
```bash
pytest --browser webkit
```

## CI/CD Pipeline

GitHub Actions automatically executes the automation suite.

The pipeline performs:

- Install Python dependencies
- Install Playwright browsers
- Execute tests across Chromium, Firefox, and WebKit
- Generate HTML reports
- Upload test artifacts

## Test Coverage

| Feature | Status |
|---|---|
| Successful Login | ✅ |
| Invalid Login | ✅ |
| Inventory Validation | ✅ |
| Add Product to Cart | ✅ |
| Checkout Workflow | ✅ |
