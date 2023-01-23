from model.group import Group


def test_modify_group(app):
    group = Group(name="test", header="test1", footer="test2")
    if app.group.count() == 0:
        app.group.add(Group(name="Empty", header="empty1", footer="empty2"))
    old_groups = app.group.get_groups_list()
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_groups_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

