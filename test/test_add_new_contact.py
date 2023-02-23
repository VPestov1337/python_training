from model.contact import Contact


def test_add_new_contact(app, db, json_contacts, check_ui):
    new_contact = json_contacts
    old_contacts = db.get_contacts_list()
    app.contact.add_new(new_contact)
    new_contacts = db.get_contacts_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)










