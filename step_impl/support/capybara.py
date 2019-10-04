import capybara
from getgauge.python import custom_screen_grabber

capybara.app = None  # Tell capybara not to spin up a server

# TODO: this should depend on environment variables/command line parameters
capybara.app_host = "https://www.preview.marketplace.team"

capybara.default_driver = "selenium_chrome_headless"

@capybara.register_driver("selenium_chrome_headless")
def init_selenium_chrome_headless_driver(app):
    from capybara.selenium.driver import Driver
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.headless = True

    driver = Driver(app, browser="chrome", options=options)
    window = driver.current_window_handle
    driver.resize_window_to(window, 1366, 768)

    return driver


@custom_screen_grabber
def take_screenshot():
    current_driver = capybara.current_driver or capybara.default_driver
    if "selenium" in current_driver:
        return capybara.current_session().driver.browser.get_screenshot_as_png()
    else:
        return _take_screenshot()
