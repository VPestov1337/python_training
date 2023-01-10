

def test_modify_contact(app):
    app.session.login()
    app.contact.modify_contact(attributesDict={"firstname": "lol", "middlename": "kek", "lastname": "TEST"})
    app.session.logout()

