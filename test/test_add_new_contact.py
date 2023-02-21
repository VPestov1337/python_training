from model.contact import Contact


def test_add_new_contact(app, json_contacts):
    new_contact = json_contacts
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new(new_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)










