from selenium.webdriver.common.by import By


class Locator_Page:
    USER_NAME_TEXTBOX = (By.XPATH, "//input[@id='Identifier']")
    PASSWORD_TEXTBOX = (By.XPATH, "//input[@id='Password']")

    #submit_first_login
    SUBMIT_BUTTON_SECURE_LOGIN = (By.XPATH, "//input[@type='submit']")

