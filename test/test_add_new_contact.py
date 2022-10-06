from model.contact import Contact


def test_add_new_contact(app):
    app.session.login("admin", "secret")
    new_contact = Contact(address="Saint-Petersburg", bday="22", bmonth="July", byear="2000", company="Company",
                          email="Email@kek.com", firstname="Ivan", lastname="Ivanov", title="Worker",
                          work_phone="555-555", aday="25", amonth="August", ayear="2018")
    app.contact.add_new(new_contact)
    app.session.logout()


def test_modify_contact(app):
    app.session.login()
    app.contact.modify_contact(attributesArray=['firstname', 'middlename', 'lastname', 'nickname', 'company',
                                                      'email', 'title', 'work'])
    app.session.logout()


def test_delete_contact(app):
    app.session.login()
    app.contact.delete_contact()
    app.session.logout()




