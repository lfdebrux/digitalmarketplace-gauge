
import json

from capybara.dsl import page
from getgauge.python import step

from step_impl.util.forms import fill_in_multipage_form


@step("Create a requirement called <requirement_title>")
def fill_in_requirement_title(requirement_title):
    page.click_button("Create requirement")
    page.fill_in("title", value=requirement_title)
    page.click_button("Save and continue")


@step("Write the requirements from <requirements_json>")
def fill_in_requirements(requirements_json):
    requirements = json.loads(requirements_json)
    fill_in_multipage_form(page, requirements)


@step("Set the requirement to be open for <value>")
def fill_in_how_long_your_requirement_will_be_open_for(value):
    page.click_link("Set how long your requirements will be open for")
    page.choose(value)
    page.click_button("Save and continue")


@step("Set how suppliers will be evaluated from <evaluation_json>")
def fill_in_evaluation_and_shortlist_process(value):
    evaluation = json.loads(evaluation_json)

    page.click_link("Shortlist and evaluation process")

    page.click_link("Set how many specialists to evaluate")
    page.fill_in("numberOfSuppliers", evaluation["numberOfSuppliers"])
    page.click_button("Save and continue")

    page.click_link("Set evaluation weighting")
    page.fill_in("technicalWeighting", evaluation["technicalWeighting"])
    page.fill_in("culturalWeighting", evaluation["culturalWeighting"])
    page.fill_in("priceWeighting", evaluation["priceWeighting"])
    page.click_button("Save and continue")


    def fill_in_criteria(name):
        for n, criteria in enumerate(evaluation[name]):
            if n > 2:
                page.click_button(f"#{name} .list-entry-add")
            page.fill_in(f"input-{name}-{n}", critera)

    page.click_link("Set technical competence criteria")
    fill_in_criteria("essentialRequirements")
    fill_in_criteria("niceToHaveRequirements")
    page.click_button("Save and continue")

    page.click_link("Choose cultural fit criteria")
    fill_in_criteria("culturalFitCriteria")


@step("Review and publish the requirement")
def review_and_publish_requirement():
    page.click_link("Review and publish your requirements")
    # page.click_button("")


@step("The opportunity <title> is listed")
def find_opportunity(title):
    pass
