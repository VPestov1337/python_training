import random


def test_add_contact_to_group(app, db, orm):
    contacts_list = db.get_contacts_list()
    groups_list = db.get_groups_list()
    contact = random.choice(contacts_list)
    group = random.choice(groups_list)
    app.contact.add_contact_to_group(contact.id, group.id)
    assert contact in orm.get_contacts_in_group(group)

