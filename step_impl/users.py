
from getgauge.python import data_store, step


@step("With a buyer user")
def get_buyer_user():
    """Find a buyer user to use for a specification"""
    # TODO: get buyer user using api
    data_store.spec["buyer"] = {
        "username": "19549@user.marketplace.team",
        "password": "Password1234",
    }

@step("As the buyer user")
def login_as_buyer_user():
    user = data_store.spec["buyer"]


@step("With a supplier user on the <lot_name> lot of the <framework_name> framework")
def get_supplier_user(lot_name, framework_name):
    pass
