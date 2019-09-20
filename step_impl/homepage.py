
from getgauge.python import step

from step_impl.pages.homepage import Homepage


homepage = Homepage()


@step(["Open the Digital Marketplace homepage", "From the Digital Marketplace homepage"])
def visit_homepage():
    homepage.visit()


@step("The homepage should be the start of all Digital Marketplace journeys")
def check_homepage_links():
    assert homepage.has_g_cloud_link()
    assert homepage.has_crown_hosting_link()
    assert homepage.has_supply_link()
    # assert homepage.has_digital_outcomes_and_specialists_links()
