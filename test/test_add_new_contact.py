from model.contact import Contact
import string
import random
import pytest


def random_contact():
    return Contact(random_string("firstname",10), random_string("lastname", 10), random_string("company", 15),
            address=random_string("address", 10), work_phone=random_phone(8), phone2=random_phone(5),
            email2=random_email(5), email=random_email(4), email3=random_email(8), mobilephone=random_phone(9),
            homephone=random_phone(6), amonth=Contact.months[random.randrange(1, 13)], aday=str(random.randrange(1, 32)),
            bmonth=Contact.months[random.randrange(1, 13)], bday=str(random.randrange(1, 32)), byear=str(random.randrange(1900,2010)),
            middlename=random_string("middlename", 6), nickname=random_string("nickname", 9),
            title=random_string("title", 12))

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(len):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    firsthalf = "".join([random.choice(symbols) for i in range(random.randrange(len))])
    return "email" + firsthalf + "@" + firsthalf[::-1] + ".com"

def random_phone(len):
    return "".join([random.choice(string.digits) for i in range(random.randrange(len))])

testdata = [random_contact() for i in range(5)]

@pytest.mark.parametrize("new_contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, new_contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new(new_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)










