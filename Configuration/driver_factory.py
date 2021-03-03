from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class DriverFactory:

    @staticmethod
    def get_driver(browser):
        # browser instance creation
        if browser=="chrome":
            # parameters for web driver
            options=webdriver.ChromeOptions()
            #this paramter handle Uncertificate websites
            options.add_argument('ignore-certificate-errors')
            options.add_argument("start-maximized")
            #intinaling and opening browser
            return webdriver.Chrome(ChromeDriverManager().install(),options=options)

        # if browser=="firefox":
        #     options=webdriver.FirefoxOptions()
        #     options.add_argument("start-maximized")
        #     return webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
        raise Exception("Please provide valid driver name")