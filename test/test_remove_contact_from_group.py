import random


def test_remove_contact_from_group(app, db, orm):
    groups_list = orm.get_non_empty_groups_list()
    group = random.choice(groups_list)
    contacts_in_group = orm.get_contacts_in_group(group)
    contact = random.choice(contacts_in_group)
    app.contact.remove_contact_from_group(contact.id, group.id)
    assert contact in orm.get_contacts_not_in_group(group)

