import random
from random import randrange

from model.group import Group


def test_del_some_group(app, db, check_ui):
    if len(db.get_groups_list()) == 0:
        app.group.add(Group(name="test", footer="test", header="test"))
    old_groups = db.get_groups_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_groups_list()
    old_groups.remove(group)
    assert new_groups == old_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)