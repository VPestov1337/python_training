from model.contact import Contact
import string
import random
import pytest




@pytest.mark.parametrize("new_contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, new_contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new(new_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)










