from model.group import Group



def test_del_group(app):
    if app.group.count() == 0:
        app.group.add(Group(name="test", footer="test", header="test"))
    old_groups = app.group.get_groups_list()
    app.group.delete_first_group()
    new_groups = app.group.get_groups_list()
    old_groups[0:1] = []
    assert new_groups == old_groups
