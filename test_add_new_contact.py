import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.open_home_page()
    app.login("admin", "secret")
    new_contact = Contact(address="Saint-Petersburg", bday="22", bmonth="July", byear="2000", company="Company",
                          email="Email@kek.com", firstname="Ivan", lastname="Ivanov", title="Worker",
                          work_phone="555-555", aday="25", amonth="August", ayear="2018")
    app.add_new_contact(new_contact)
    app.open_home_page()
    app.logout()

