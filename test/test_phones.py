import re

def test_phones_on_home_page(app):
    contact_fr_hm_pg = app.contact.get_contacts_list()[0]
    contact_fr_ed_pg = app.contact.get_contact_info_from_edit_page(0)
    assert contact_fr_hm_pg.all_phones_from_homepage == merge_phones_like_on_hm_pg(contact_fr_ed_pg)

def test_phone_on_contact_view_page(app):
    contact_fr_vw_pg = app.contact.get_contact_from_view_page(0)
    contact_fr_ed_pg = app.contact.get_contact_info_from_edit_page(0)
    assert contact_fr_ed_pg.homephone == contact_fr_vw_pg.homephone
    assert contact_fr_ed_pg.work_phone == contact_fr_vw_pg.work_phone
    assert contact_fr_ed_pg.phone2 == contact_fr_vw_pg.phone2

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_hm_pg(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.homephone, contact.mobilephone,
                                                                        contact.work_phone, contact.phone2]))))

