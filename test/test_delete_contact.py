from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Ivan"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_contact()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)



