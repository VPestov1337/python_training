from random import randrange

from model.group import Group


def test_del_some_group(app):
    if app.group.count() == 0:
        app.group.add(Group(name="test", footer="test", header="test"))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_groups_list()
    old_groups[index:index+1] = []
    assert new_groups == old_groups
