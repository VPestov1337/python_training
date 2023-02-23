from random import randrange

from model.group import Group


def test_modify_group(app, db, check_ui):
    group = Group(name="test151", header="test1", footer="test2")
    if app.group.count() == 0:
        app.group.add(Group(name="Empty", header="empty1", footer="empty2"))
    old_groups = db.get_groups_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group, group.id)
    new_groups = db.get_groups_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)

