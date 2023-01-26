from sys import maxsize


class Contact:
    def __init__(self, firstname="", lastname="", company="", title="", address="", work_phone="", email="", bday="15",
                 bmonth="January", byear="2000", middlename="", nickname="", aday="5", amonth="July", ayear="2018",
                 email2="", email3="", mobilephone="", homephone="", fax="", homepage="", address2="",
                 phone2="", notes="", id=None, all_phones_from_homepage=None, all_emails=None):

        self.notes = notes
        self.phone2 = phone2
        self.byear = byear
        self.bmonth = bmonth
        self.bday = bday
        self.email = email
        self.email3 = email3
        self.email2 = email2
        self.address2 = address2
        self.ayear = ayear
        self.amonth = amonth
        self.homepage = homepage
        self.aday = aday
        self.fax = fax
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.nickname = nickname
        self.middlename = middlename
        self.work_phone = work_phone
        self.address = address
        self.title = title
        self.company = company
        self.lastname = lastname
        self.firstname = firstname
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails = all_emails

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
            and self.lastname == other.lastname

    def id_or_max(self):
        if self.id is not None:
            return int(self.id)
        else:
            return maxsize
