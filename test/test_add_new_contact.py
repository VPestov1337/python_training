from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contacts_list()
    new_contact = Contact(address="Saint-Petersburg", bday="22", bmonth="July", byear="2000", company="Company",
                          email="Email@kek.com", firstname="Ivan", lastname="Ivanov", title="Worker",
                          work_phone="555-555", aday="25", amonth="August", ayear="2018")
    app.contact.add_new(new_contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)










