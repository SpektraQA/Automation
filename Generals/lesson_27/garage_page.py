from playwright.sync_api import Page

class GaragePage:
    def __init__(self, page: Page):
        self.page = page

        # авторизация
        self.sign_in_button = page.get_by_role("button", name="Sign In")
        self.email_input = page.get_by_role("textbox", name="Email")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

        # добавление машины
        self.add_car_button = page.get_by_role("button", name="Add car")
        self.brand_select = page.get_by_label("Brand")
        self.model_select = page.get_by_label("Model")
        self.mileage_input = page.get_by_role("spinbutton", name="Mileage")
        self.dialog = page.get_by_role("dialog")
        self.km_text = page.get_by_text("km")
        self.add_button = page.get_by_role("button", name="Add")

        # меню карточки машины (апдейт / удаление)
        self.car_menu_button = page.get_by_role("button").nth(5)
        self.save_button = page.get_by_role("button", name="Save")
        self.remove_car_button = page.get_by_role("button", name="Remove car")
        self.remove_button = page.get_by_role("button", name="Remove")

    def open(self):
        self.page.goto("https://guest:welcome2qauto@qauto.forstudy.space/")

    def login(self, email: str, password: str):
        self.sign_in_button.click()
        self.email_input.click()
        self.email_input.fill(email)
        self.password_input.click()
        self.password_input.fill(password)
        self.login_button.click()

    def add_car(self, brand: str, model: str, mileage: str):
        self.add_car_button.click()
        self.brand_select.select_option(brand)
        self.model_select.select_option(model)
        self.mileage_input.click()
        self.mileage_input.fill(mileage)
        self.dialog.click()
        self.km_text.click()
        self.add_button.click()

    def update_mileage(self, new_mileage: str):
        self.car_menu_button.click()
        self.mileage_input.click()
        self.mileage_input.fill(new_mileage)
        self.save_button.click()

    def delete_first_car(self):
        self.car_menu_button.click()
        self.remove_car_button.click()
        self.remove_button.click()