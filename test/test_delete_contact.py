import random
from random import randrange

from model.contact import Contact


def test_delete_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Ivan"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contacts_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(),
                                                                     key=Contact.id_or_max)



