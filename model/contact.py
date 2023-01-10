class Contact:

    def __init__(self, firstname, lastname, company, title, address, work_phone, email, bday, bmonth, byear,
                 middlename="", nickname="", aday="", amonth="", ayear="", email2="", email3="",
                 mobilephone="", homephone="", fax="", homepage="", address2="", phone2="", notes=""):
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

    atrLocDict = {                 #dict for attributes-locators translation
    "firstname": "firstname",
    "middlename": "middlename",
    "lastname": "lastname",
    "nickname": "nickname",
    "title": "title",
    "company": "company",
    "address": "address",
    "homephone": "home",
    "mobilephone": "mobile",
    "work_phone": "work",
    "fax": "fax",
    "email": "email",
    "email2": "email2",
    "email3": "email3",
    "homepage": "homepage",
    "bday": "bday",
    "bmonth": "bmonth",
    "byear": "byear",
    "aday": "aday",
    "ayear": "ayear",
    "address2": "address2",
    "phone2": "phone2",
    "notes": "notes"

    }