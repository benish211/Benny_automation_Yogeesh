import time

from Locators.login_locator import Locator_Page

class Login_Page:
    def __init__(self, driver):
        self.driver=driver

    def open_page(self):
        self.driver.get("https://zschool.co.il/")

    def get_user_inputes(self, username, password):
        time.sleep(2)
        self.driver.find_element(*Locator_Page.USER_NAME_TEXTBOX).click()
        self.driver.find_element(*Locator_Page.USER_NAME_TEXTBOX).send_keys(username)
        # clear and send the password
        self.driver.find_element(*Locator_Page.PASSWORD_TEXTBOX).click()
        self.driver.find_element(*Locator_Page.PASSWORD_TEXTBOX).send_keys(password)
        # click at submit button
        self.driver.find_element(*Locator_Page.SUBMIT_BUTTON_SECURE_LOGIN).click()





