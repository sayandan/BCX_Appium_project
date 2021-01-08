from selenium import webdriver
from appium import webdriver
import pytest

# fixtures are functions which will run before each test function to which it is applied.
# it is used to feed some data to tests such as db connections, url etc. to access the fixture function the tests have
# to mention the fixture name as input parameter


@pytest.fixture(scope='class')
def init_driver(request):

    desired_capabilities = {
        "deviceName": "Android Emulator",
        "platformName": "Android",
        "appPackage": "com.bcx.mobile.transact",
        "appActivity": "crc64e72c99f345d22f2f.SplashActivity",
        "autoGrantPermissions": "true",
        "noReset": "true"
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    driver.implicitly_wait(30)
    # driver.find_element_by_xpath("//android.widget.EditText[@text='URL']").send_keys('https://testmosque.mossbros.co.uk:9946')
    # driver.find_element_by_xpath("//android.widget.EditText[@text='Tenant ID']").send_keys('2')
    # driver.find_element_by_id('com.bcx.mobile.transact:id/save_button').click()
    request.cls.driver = driver
    # yield
    # driver.quit()


# ---------------PyTest HTML report  create report using the  CLI command --html=..\Reports\reports.html
# it is hook for adding environment ingo to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'BCX_Appium Transact Appium'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Siva'


# it is  hook for delete/modify environment info from html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

