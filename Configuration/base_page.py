import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver

from Locators.login_locator import Locator_Page

from Configuration.driver_factory import DriverFactory
class BasePage(DriverFactory):
    def __init__(self, driver):
        self.driver=driver

    # Explicit Waits generic for all project

    try:
        # wait 10 seconds before looking for element
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
    finally:
        # else quit
        driver.quit()
    #should insert login function:


    #should insert call to JSON with user name and password