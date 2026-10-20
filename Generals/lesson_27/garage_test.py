import os
import pytest
from playwright.sync_api import Page
from garage_page import GaragePage

EMAIL = os.getenv("USER_LOGIN")
PASSWORD = os.getenv("USER_PASSWORD")

@pytest.fixture
def garage(page: Page) -> GaragePage:
    gp = GaragePage(page)
    gp.open()
    gp.login(EMAIL, PASSWORD)
    return gp

def test_create_car(garage: GaragePage) -> None:
    garage.add_car("3: 4", "7: 18", "30")


def test_update_mileage_car(garage: GaragePage) -> None:
    garage.update_mileage("10000")

def test_delete_car(garage: GaragePage) -> None:
    garage.delete_first_car()