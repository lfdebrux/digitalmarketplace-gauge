
from step_impl.pages.base import BasePage, Element, Section


class DigitalOutcomesAndSpecialistsLinks(Section):
    digital_specialists_link = Element("link", "Find an individual specialist")
    digital_outcomes_link = Element("link", "Find a team to provide an outcome")
    user_research_participants_link = Element("link", "Find user research participants")
    user_research_studios_link = Element("link", "Find a user research lab")
    opportunities_link = Element("link", "View Digital Outcomes and Specialists opportunities")


class Homepage(BasePage):
    URL = "/"

    crown_hosting_link = Element("link", "Buy physical datacentre space")
    digital_outcomes_and_specialists_links = DigitalOutcomesAndSpecialistsLinks("ul.browse-list")
    g_cloud_link = Element("link", "Find cloud hosting, software and support")

    supply_link = Element("link", "Become a supplier")
