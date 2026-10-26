import os
import allure
import pytest
from playwright.sync_api import Page, expect
from garage_page import GaragePage

EMAIL = os.getenv("USER_LOGIN")
PASSWORD = os.getenv("USER_PASSWORD")

@pytest.fixture
def garage(page: Page) -> GaragePage:
    gp = GaragePage(page)
    gp.open()
    gp.login(EMAIL, PASSWORD)
    return gp

@allure.feature("Garage CRUD")
def test_create_car(garage: GaragePage) -> None:
    with allure.step("Add a new car with brand, model and mileage"):
        garage.add_car("3: 4", "7: 18", "30")
    with allure.step("Verify the add car dialog closed after submission"):
        expect(garage.dialog).to_be_hidden()

@allure.feature("Garage CRUD")
def test_update_mileage_car(garage: GaragePage) -> None:
    with allure.step("Update the car's mileage"):
        garage.update_mileage("10000")
    with allure.step("Verify the save button is no longer visible (form closed)"):
        expect(garage.save_button).to_be_hidden()


@allure.feature("Garage CRUD")
def test_delete_car(garage: GaragePage) -> None:
    with allure.step("Delete the first car in the garage"):
        garage.delete_first_car()
    with allure.step("Verify the remove confirmation button is no longer visible"):
        expect(garage.remove_button).to_be_hidden()