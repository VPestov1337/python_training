from random import randrange
import re

def test_contact_fields_on_home_page(app):
    app.contact.goToContactsPage()
    contact_list = app.contact.get_contacts_list()
    index = randrange(len(contact_list))
    contact_fr_hm_pg = contact_list[index]
    contact_fr_ed_pg = app.contact.get_contact_info_from_edit_page(index)
    assert contact_fr_hm_pg.all_emails == merge_emails_like_on_home_page(contact_fr_ed_pg)
    assert contact_fr_hm_pg.address == contact_fr_ed_pg.address
    assert contact_fr_hm_pg.all_phones_from_homepage == merge_phones_like_on_hm_pg(contact_fr_ed_pg)
    assert contact_fr_hm_pg.firstname == contact_fr_ed_pg.firstname
    assert contact_fr_hm_pg.lastname == contact_fr_ed_pg.lastname


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_hm_pg(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.homephone, contact.mobilephone,
                                                                        contact.work_phone, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
     return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                                              [contact.email, contact.email2,
                                                                        contact.email3])))