from model.contact import Contact
import random
import string
import getopt
import sys
import jsonpickle
import os


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


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "if":
        f = a

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

testdata = [random_contact() for i in range(n)]
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
