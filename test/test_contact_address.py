from random import randrange


def test_contact_address_on_home_page(app):
    app.contact.goToContactsPage()
    contact_list = app.contact.get_contacts_list()
    index = randrange(len(contact_list))
    contact_fr_hm_pg = contact_list[index]
    contact_fr_ed_pg = app.contact.get_contact_info_from_edit_page(index)
    assert contact_fr_hm_pg.address == contact_fr_ed_pg.address


