from random import randrange
import re

from model.contact import Contact


def test_contact_fields_on_home_page(app, db):
    app.contact.goToContactsPage()
    contact_list_fr_hm = sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
    contact_list_fr_db = sorted(db.get_contacts_list(), key=Contact.id_or_max)
    for i in range(len(contact_list_fr_hm)):
        assert contact_list_fr_hm[i].all_emails == merge_emails_like_on_home_page(contact_list_fr_db[i])
        assert contact_list_fr_hm[i].address == contact_list_fr_db[i].address
        assert contact_list_fr_hm[i].all_phones_from_homepage == merge_phones_like_on_hm_pg(contact_list_fr_db[i])
        assert contact_list_fr_hm[i].firstname == contact_list_fr_db[i].firstname
        assert contact_list_fr_hm[i].lastname == contact_list_fr_db[i].lastname


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
