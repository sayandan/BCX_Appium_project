from PageObjects.Login import Login
from Utilities.BaseTest import BaseTest
from Utilities.TestData import TestData


class TestLogin(BaseTest):

    def test_01_login_as_manager(self):
        self.login_page = Login(self.driver)
        footer_msg = self.login_page.login(TestData.MANAGER_LOGIN, TestData.MANAGER_PASSWORD)
        print(footer_msg)
        if 'User' in footer_msg:
            assert True
        else:
            self.driver.save_screenshot('../Reports/test_01_login_as_manager.png')
            assert False

    # def test_02_login_as_cashier(self):
    #     self.login_page = Login(self.driver)
    #     footer_msg = self.login_page.login(TestData.CASHIER_LOGIN, TestData.CASHIER_PASSWORD)
    #     print(footer_msg)
    #     assert 'User' in footer_msg
