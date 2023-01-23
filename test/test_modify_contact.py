
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Ivan"))
    old_contacts = app.contact.get_contacts_list()
    new_contact = Contact(firstname=old_contacts[0].firstname, lastname=old_contacts[0].lastname, id=old_contacts[0].id)
    new_contact.firstname = "MODIFIED"
    app.contact.modify_contact(new_contact)
    old_contacts[0] = new_contact
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)








