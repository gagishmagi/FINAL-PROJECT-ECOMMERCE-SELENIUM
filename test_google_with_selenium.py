
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService



@pytest.fixture()
def driver():
    firefox_driver_binary = "./drivers/geckodriver"
    ser_firefox = FirefoxService(firefox_driver_binary)
    firefox_options = FireFoxOptions()

    brave_path = "/usr/bin/brave-browser"
    options = webdriver.ChromeOptions()
    options.binary_location = brave_path

    browser_name = "firefox"

    # if isinstance(browserName,list):
    #     for browser_name in browserName:
    if browser_name == "firefox-webdriver":
        driver = webdriver.Firefox(service=ser_firefox)
    elif browser_name == "firefox":
        firefox_options.add_argument("--headless")
        dc = {
            "browserName": "firefox",
            # "browserVersion": "101.0.1(x64)",
            "platformName": "LINUX"
        }
        driver = webdriver.Remote("http://localhost:4444",desired_capabilities=dc, options=firefox_options)

    elif browser_name == "brave":
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        dc = {
            "browserName": "chrome",
            "platformName": "LINUX"
        }
        driver = webdriver.Remote("http://localhost:4444",desired_capabilities=dc,options=options)

    elif browser_name == "chrome":
        dc = {
            "browserName": "chrome",
            "platformName": "LINUX"
        }
        driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc)

    elif browser_name == "firefox-mobile":
        firefox_options = FireFoxOptions()
        firefox_options.add_argument("--width=375")
        firefox_options.add_argument("--height=812")
        firefox_options.set_preference("general.useragent.override", "userAgent=Mozilla/5.0 "
                                                                     "(iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like "
                                                                     "Gecko) CriOS/101.0.4951.44 Mobile/15E148 Safari/604.1")
        # firefox_options.set_preference("general.useragent.override", "Nexus 7")

        driver = webdriver.Firefox(service=ser_firefox, options=firefox_options)

    elif browser_name == "android-emulator":
        dc = {
            "platformName": "Android",
            "platformVersion": "8.1.0",
            "deviceName": "Android Emulator",
            # "platformVersion": "11.0.0",
            # "deviceName": "1aaa4ea80404",
            "automationName": "Appium",
            # "app": "com.android.chrome",
            "browserName": "Chrome"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)

    elif browser_name == "android-phone":
        dc = {
            "platformName": "Android",
            "platformVersion": "11.0.0",
            "deviceName": "1aaa4ea80404",
            "automationName": "Appium",
            "browserName": "Chrome"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)
    else:
        raise Exception("driver doesn't exists")











    # firefox_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')

    # capabilities = {
    #     'browserName': 'firefox',
    #     'firefoxOptions': {
    #         'mobileEmulation': {
    #             'deviceName': 'iPhone X'
    #         }
    #     }
    # }
    # user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"

    # profile = webdriver.FirefoxProfile()
    # profile.set_preference("general.useragent.override", user_agent)
    # driver = webdriver.Firefox(profile)


    # parent_handle = driver.current_window_handle
    # for handle in driver.window_handles:
    #     if parent_handle != handle:
    #         driver.switch_to(handle)

    yield driver
    driver.close()


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
# driver = webdriver.Chrome(chrome_options = chrome_options)




def test_google_page_title(driver):
    driver.get('https://www.google.com')
    title = driver.title
    # driver.save_screenshot("test_google_title.png")
    assert title == str.title("google!")

