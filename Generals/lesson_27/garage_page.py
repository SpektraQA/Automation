from playwright.sync_api import Page

class GaragePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://guest:welcome2qauto@qauto.forstudy.space/")

    def login(self, email: str, password: str):
        self.page.get_by_role("button", name="Sign In").click()
        self.page.get_by_role("textbox", name="Email").click()
        self.page.get_by_role("textbox", name="Email").fill(email)
        self.page.get_by_role("textbox", name="Password").click()
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def add_car(self, brand: str, model: str, mileage:str):
        self.page.get_by_role("button", name="Add car").click()
        self.page.get_by_label("Brand").select_option(brand)
        self.page.get_by_label("Model").select_option(model)
        self.page.get_by_role("spinbutton", name="Mileage").click()
        self.page.get_by_role("spinbutton", name="Mileage").fill(mileage)
        self.page.get_by_role("dialog").click()
        self.page.get_by_text("km").click()
        self.page.get_by_role("button", name="Add").click()

    def update_mileage(self, new_mileage: str):
        self.page.get_by_role("button").nth(5).click()
        self.page.get_by_role("spinbutton", name="Mileage").click()
        self.page.get_by_role("spinbutton", name="Mileage").fill(new_mileage)
        self.page.get_by_role("button", name="Save").click()

    def delete_first_car(self):
        self.page.get_by_role("button").nth(5).click()
        self.page.get_by_role("button", name="Remove car").click()
        self.page.get_by_role("button", name="Remove").click()
