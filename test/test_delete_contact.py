import time

def test_delete_contact(app):
    app.session.login()
    app.contact.delete_contact()
    app.session.logout()



