import base64
import os
import time

from selenium.webdriver.common.by import By

from PageObjects.Login import Login
from Utilities.BasePage import BasePage
from Utilities.TestData import TestData


class SalesScreen(BasePage):
    """By locators"""
    USER_NAME = (By.ID, "com.bcx.mobile.transact:id/username_validation_input")
    PASSWORD = (By.ID, "com.bcx.mobile.transact:id/password_validation_input")
    LOGIN_BUTTON = (By.ID, "com.bcx.mobile.transact:id/login_button")
    FOOTER_CONFIRM_MSG = (By.ID, 'com.bcx.mobile.transact:id/footer_center_text')
    """Hamburger menu locators"""
    HAMBURGER_MENU = (By.XPATH, "//android.widget.ImageButton[@content-desc='Open navigation drawer']")
    HAMBURGER_CLOSE = (By.ID, 'com.bcx.mobile.transact:id/close_button')

    """hamburger or home screen menus"""
    PRODUCT_LOOKUP_BUTTON = (By.XPATH, "//android.widget.TextView[@text='Product Lookup']")
    SALES_SCREEN_BUTTON = (By.XPATH, "//android.widget.TextView[@text='Sales Screen']")
    RETRIEVE_SALE_BUTTON = (By.XPATH, "//android.widget.TextView[@text='Retrieve Sale']")
    ABOUT_BUTTON = (By.XPATH, "//android.widget.TextView[@text='About']")
    LOGOUT_BUTTON = (By.XPATH, "//android.widget.TextView[@text='Logout']")

    """sales screen locators"""
    BARCODE_INPUT = (By.ID, 'com.bcx.mobile.transact:id/code_input')
    OPTIONS_BUTTON = (By.ID, 'com.bcx.mobile.transact:id/button_options')
    TENDER_BUTTON = (By.ID, 'com.bcx.mobile.transact:id/btn_tender')
    SUSPEND_BUTTON = (By.ID, 'com.bcx.mobile.transact:id/btn_suspend')
    SUSPEND_CONFIRM_OK = (By.ID, 'com.bcx.mobile.transact:id/confirm_button')
    SUSPEND_CONFIRM_CANCEL = (By.ID, 'com.bcx.mobile.transact:id/cancel_button')
    SUSPENDED_CONTINUE_BUTTON = (By.ID, 'com.bcx.mobile.transact:id/confirm_button')

    """Kebab"""
    KEBAB_MENU = (By.XPATH, "//android.widget.TextView[@content-desc = 'Options']")
    KEBAB_CLOSE_BUTTON = (By.ID, 'com.bcx.mobile.transact:id/close_button')
    KEBAB_TRANSACTION_VOID = (By.XPATH, "//android.widget.TextView[@text='Transaction Void']")
    KEBAB_PRODUCT_SEARCH = (By.XPATH, "//android.widget.TextView[@text='Product Search']")
    KEBAB_SUBTOTAL = (By.XPATH, "//android.widget.TextView[@text='Subtotal']")
    KEBAB_SUSPEND_SALE = (By.XPATH, "//android.widget.TextView[@text='Suspend Sale']")
    KEBAB_TENDER = (By.XPATH, "//android.widget.TextView[@text='Tender']")

    VOID_OPTION_01 = (By.XPATH, "//android.widget.TextView[@text='01']")
    VOID_OPTION_02 = (By.XPATH, "//android.widget.TextView[@text='02']")

    CONFIRMATION_OK_TICK = (By.ID, "com.bcx.mobile.transact:id/confirm_button")
    CONFIRMATION_CANCEL_CROSS = (By.ID, "com.bcx.mobile.transact:id/cancel_button")
    CONTINUE_CONFIRMATION = (By.XPATH, "//android.widget.Button[@text='CONTINUE']")

    AUTHORISATION_USERNAME = (By.XPATH, "//android.widget.EditText[@text='Username']")
    AUTHORISATION_PASSWORD = (By.XPATH, "//android.widget.EditText[@text='Password']")
    AUTHORISE_BUTTON = (By.ID, 'com.bcx.mobile.transact:id/authorize_button')

    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)

    """action methods"""
    def login(self, user, password):
        self.do_send_keys(self.USER_NAME, user)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

    def authorise(self, user, password):
        self.do_send_keys(self.AUTHORISATION_USERNAME, user)
        self.do_send_keys(self.AUTHORISATION_PASSWORD, password)
        self.do_click(self.AUTHORISE_BUTTON)

    # Homepage button actions or hamburger button actions
    def click_sales_screen(self):
        self.do_click(self.SALES_SCREEN_BUTTON)

    def click_product_lookup(self):
        self.do_click(self.PRODUCT_LOOKUP_BUTTON)

    def click_retrieve_sale(self):
        self.do_click(self.RETRIEVE_SALE_BUTTON)

    def click_logout(self):
        self.do_click(self.LOGOUT_BUTTON)

    # Sales screen actions
    def scan_products(self, *skus):
        for sku in skus:
            self.do_send_keys(self.BARCODE_INPUT, sku + '\n')

    def select_void01(self):
        self.do_click(self.VOID_OPTION_01)

    def select_void02(self):
        self.do_click(self.VOID_OPTION_02)

    def select_confirmation_ok(self):
        self.do_click(self.CONFIRMATION_OK_TICK)

    def select_confirmation_cancel(self):
        self.do_click(self.CONFIRMATION_CANCEL_CROSS)

    def select_continue(self):
        self.do_click(self.CONTINUE_CONFIRMATION)

    # Kebab menu actions
    def click_kebab_menu(self):
        self.do_click(self.KEBAB_MENU)

    def click_kebab_tran_void(self):
        self.do_click(self.KEBAB_TRANSACTION_VOID)

    def click_kebab_product_search(self):
        self.do_click(self.KEBAB_PRODUCT_SEARCH)

    def click_kebab_subtotal(self):
        self.do_click(self.KEBAB_SUBTOTAL)

    def click_kebab_suspend_sale(self):
        self.do_click(self.KEBAB_SUSPEND_SALE)

    def click_kebab_tender(self):
        self.do_click(self.KEBAB_TENDER)









    def sales_screen(self):

        """Start recording video"""
        # self.driver.start_recording_screen()

        self.login_page = Login(self.driver)
        self.login_page.login(TestData.MANAGER_LOGIN, TestData.MANAGER_PASSWORD)
        # self.do_click(self.HAMBURGER_MENU)
        self.do_click(self.SALES_SCREEN_BUTTON)
        self.do_send_keys(self.BARCODE_INPUT, '9627890153206' + '\n')
        # self.do_click(self.OPTIONS_BUTTON)



        """stop recording video"""
        # video_raw = self.driver.stop_recording_screen()
        # video_name = self.driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")
        # file_path = os.path.join('../Reports/' + video_name + '.mp4')
        # with open(file_path, 'wb') as vd:
        #     vd.write(base64.b64decode(video_raw))

        """
        video recording steps:
        @driver method
            - start_recording_screen()
            - stop_recording_screen()
        @python
            - convert base-64 into media mp4 file
        @steps
            1. create file path (using os.path.join director, filename)
            2. save the video base-64
            3. convert raw file to mp4 using ( with <expression> as <variable>: decode base64 file)
        
        """
