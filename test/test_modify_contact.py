from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Ivan"))
    app.contact.modify_contact(attributesArray=['firstname', 'middlename', 'lastname', 'nickname', 'company',
                                                'email', 'title', 'work'])
