from Locators.login_locator import Locator_Page


class Main_Page_Login:

    def __init__(self, driver):
        self.driver = driver

    def user_inputs_main_login(self, username, password):
        self.driver.find_element(*Locator_Page.LOGIN_BUTTON).click()

        self.driver.find_element(*Locator_Page.MAIN_USER_NAME_TEXTBOX).click()
        self.driver.find_element(*Locator_Page.MAIN_USER_NAME_TEXTBOX).send_keys(username)

        self.driver.find_element(*Locator_Page.MAIN_PASSWORD_TEXTBOX).click()
        self.driver.find_element(*Locator_Page.MAIN_PASSWORD_TEXTBOX).send_keys(password)
