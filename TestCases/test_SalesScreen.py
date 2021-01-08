from PageObjects.SalesScreen import SalesScreen
from Utilities.BaseTest import BaseTest
from Utilities.TestData import TestData


class TestSalesScreen(BaseTest):

    def test_01_sales_tran_void01(self):
        self.sales_page = SalesScreen(self.driver)
        self.sales_page.login(TestData.CASHIER_LOGIN, TestData.CASHIER_PASSWORD)
        self.sales_page.click_sales_screen()
        self.sales_page.scan_products('9627890153206', '9627890153206')
        self.sales_page.click_kebab_menu()
        self.sales_page.click_kebab_tran_void()
        self.sales_page.select_void01()
        self.sales_page.select_confirmation_cancel()
        self.sales_page.click_kebab_menu()
        self.sales_page.click_kebab_tran_void()
        self.sales_page.select_void01()
        self.sales_page.select_confirmation_ok()
        self.sales_page.select_continue()

    def test_02_sales_tran_void02(self):
        self.sales_page = SalesScreen(self.driver)
        self.sales_page.login(TestData.MANAGER_LOGIN, TestData.MANAGER_PASSWORD)
        self.sales_page.click_sales_screen()
        self.sales_page.scan_products('9627890153206', '9627890153206')
        self.sales_page.click_kebab_menu()
        self.sales_page.click_kebab_tran_void()
        self.sales_page.select_void02()
        self.sales_page.select_confirmation_cancel()
        self.sales_page.click_kebab_menu()
        self.sales_page.click_kebab_tran_void()
        self.sales_page.select_void02()
        self.sales_page.select_confirmation_ok()
        self.sales_page.authorise(TestData.CASHIER_LOGIN, TestData.CASHIER_PASSWORD)
        self.sales_page.select_continue()

    def test_03_sales_tran_tender(self):
        self.sales_page = SalesScreen(self.driver)
        self.sales_page.login(TestData.CASHIER_LOGIN, TestData.CASHIER_PASSWORD)
        self.sales_page.click_sales_screen()
        self.sales_page.scan_products('9627890153206', '9627890153206')
        self.sales_page.click_kebab_menu()
        self.sales_page.click_kebab_tender()

    def test_09_tran_not_found(self):
        self.sales_page = SalesScreen(self.driver)
        self.sales_page.login(TestData.MANAGER_LOGIN, TestData.MANAGER_PASSWORD)
        self.sales_page.click_sales_screen()
        self.sales_page.click_kebab_menu()
        self.sales_page.click_kebab_tran_void()
        self.sales_page.select_continue()
        self.sales_page.click_kebab_menu()
        self.sales_page.click_kebab_subtotal()
        self.sales_page.select_continue()
        self.sales_page.click_kebab_menu()
        self.sales_page.click_kebab_suspend_sale()
        self.sales_page.select_confirmation_ok()
        self.sales_page.select_continue()
        self.sales_page.click_kebab_menu()
        self.sales_page.click_kebab_tender()
        self.sales_page.select_continue()








