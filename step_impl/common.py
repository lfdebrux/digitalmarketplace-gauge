
from getgauge.python import step

from capybara.dsl import page


@step("Open the <link_text> page")
def visit_link(link_text):
    page.click_link(link_text)


@step("Provide an email address")
def fill_in_email_address():
    pass
