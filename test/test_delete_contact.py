from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Ivan"))

    app.contact.delete_contact()


