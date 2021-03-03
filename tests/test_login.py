from turtle import Canvas

import pytest


from Pages import login_page
from Pages.login_page import Login_Page
from Pages.main_login_PAGE import Main_Page_Login
import time

@pytest.mark.usefixtures("setup")
class TestLogIn:

    #loggin methode valid
    def test_login_passed(self):
        log_in_page=Login_Page(self.driver)
        log_in_page.open_page()
        log_in_page.get_user_inputes("beni-s@yit.co.il","qw762031")
        time.sleep(5)
    #def test_main_login(self):
        main_login=Main_Page_Login(self.driver)
        main_login.user_inputs_main_login("beni-s@yit.co.il", "qw762031")
        time.sleep(5)


