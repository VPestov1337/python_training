from random import randrange

from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Ivan"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts



