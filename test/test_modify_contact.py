from random import randrange

from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Ivan"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    new_contact = Contact(firstname=old_contacts[index].firstname, lastname=old_contacts[index].lastname, id=old_contacts[index].id)
    new_contact.firstname = "MODIFIED"
    app.contact.modify_contact_by_index(new_contact, index)
    old_contacts[index] = new_contact
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)








