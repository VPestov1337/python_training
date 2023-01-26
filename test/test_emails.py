from random import randrange


def test_emails_on_home_page(app):
    app.contact.goToContactsPage()
    contact_list = app.contact.get_contacts_list()
    index = randrange(len(contact_list))
    contact_fr_vw_pg = contact_list[index]
    contact_fr_ed_pg = app.contact.get_contact_info_from_edit_page(index)
    assert contact_fr_vw_pg.all_emails == merge_emails_like_on_home_page(contact_fr_ed_pg)


def merge_emails_like_on_home_page(contact):
     return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                                              [contact.email, contact.email2,
                                                                        contact.email3])))