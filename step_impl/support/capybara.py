
import capybara

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

    return Driver(app, browser="chrome", options=options)
