import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_non_empty_groups_list()
    for item in l:
        print(item)
    print(len(l))
    print(db.get_max_group_id())
finally:
    pass