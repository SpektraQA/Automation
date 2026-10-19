import re
from playwright.sync_api import Page, expect


def test_create_car(page: Page) -> None:
    page.goto("https://guest:welcome2qauto@qauto.forstudy.space/")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("textbox", name="Email").fill("nedzelnytskyidev+hillel02026@gmail.com")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("AYf3JtDQnAcMbnc")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Add car").click()
    page.get_by_label("Brand").select_option("3: 4")
    page.get_by_label("Model").select_option("7: 18")
    page.get_by_role("spinbutton", name="Mileage").click()
    page.get_by_role("spinbutton", name="Mileage").fill("30")
    page.get_by_role("dialog").click()
    page.get_by_text("km").click()
    page.get_by_role("button", name="Add").click()


def test_update_mileage_car(page: Page) -> None:
    page.goto("https://guest:welcome2qauto@qauto.forstudy.space/")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("nedzelnytskyidev+hillel02026@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("AYf3JtDQnAcMbnc")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button").nth(5).click()
    page.get_by_role("spinbutton", name="Mileage").click()
    page.get_by_role("spinbutton", name="Mileage").fill("10000")
    page.get_by_role("button", name="Save").click()



def test_delete_car(page: Page) -> None:
    page.goto("https://guest:welcome2qauto@qauto.forstudy.space/")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("nedzelnytskyidev+hillel02026@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("AYf3JtDQnAcMbnc")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button").nth(5).click()
    page.get_by_role("button", name="Remove car").click()
    page.get_by_role("button", name="Remove").click()
