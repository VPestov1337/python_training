import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.session.login("admin", "secret")
    new_contact = Contact(address="Saint-Petersburg", bday="22", bmonth="July", byear="2000", company="Company",
                          email="Email@kek.com", firstname="Ivan", lastname="Ivanov", title="Worker",
                          work_phone="555-555", aday="25", amonth="August", ayear="2018")
    app.contact.add_new(new_contact)
    app.session.logout()

