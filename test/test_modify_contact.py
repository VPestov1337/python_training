def test_modify_contact(app):
    app.contact.modify_contact(attributesArray=['firstname', 'middlename', 'lastname', 'nickname', 'company',
                                                'email', 'title', 'work'])
