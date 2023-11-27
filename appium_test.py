

from appium import webdriver
from appium.options.common import AppiumOptions

# Desired capabilities for the iOS app

options = {
    'platformName': 'iOS',
    'platformVersion': '15.5',
    'deviceName': 'iPad',
    'noReset': True,
    'app': "/Users/edwardaguilar/Library/Developer/Xcode/DerivedData/UIKitCatalog-dajgvhtpmifrxhetqiqcgecjsyyg/Build/Products/Debug-iphonesimulator/UIKitCatalog.app",
    'udid': "D3FC3EC2-E311-432C-9B7D-C1F7222974FF",
    'automationName': "XCUITest",
    'newCommandTimeout': 3600
}

# Initialize the driver with desired capabilities
driver = webdriver.Remote("http://localhost:4723/wd/hub", AppiumOptions)

