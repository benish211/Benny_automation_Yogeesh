from selenium.webdriver.common.by import By


class Locator_Page:
    USER_NAME_TEXTBOX = (By.XPATH, "//input[@id='Identifier']")
    PASSWORD_TEXTBOX = (By.XPATH, "//input[@id='Password']")

    #submit_first_login
    SUBMIT_BUTTON_SECURE_LOGIN = (By.XPATH, "//input[@type='submit']")

    #Locators main login page
    LOGIN_BUTTON =(By.CSS_SELECTOR, "body.page.ng-scope:nth-child(2) header.header-container.ng-scope:nth-child(3) div.menu-wrapper.desktop:nth-child(1) div.menu-container div.left-side div.not-logged-in > a.button-pill-right.button-yellow.yno-button-white.overlay.signup")

    MAIN_USER_NAME_TEXTBOX=(By.ID, "identifier")
    MAIN_PASSWORD_TEXTBOX=(By.ID,"pwd")
