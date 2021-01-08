from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage


class Login(BasePage):

    """ By Locators """
    # USER_NAME = (By.XPATH, "//android.widget.EditText[@text='Username']")
    # PASSWORD = (By.XPATH, "//android.widget.EditText[@text='Password']")
    USER_NAME = (By.ID, "com.bcx.mobile.transact:id/username_validation_input")
    PASSWORD = (By.ID, "com.bcx.mobile.transact:id/password_validation_input")
    LOGIN_BUTTON = (By.ID, "com.bcx.mobile.transact:id/login_button")
    FOOTER_CONFIRM_MSG = (By.ID, 'com.bcx.mobile.transact:id/footer_center_text')

    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)

    """action methods"""
    def login(self, user, password):
        self.do_send_keys(self.USER_NAME, user)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return self.get_element_text(self.FOOTER_CONFIRM_MSG)

