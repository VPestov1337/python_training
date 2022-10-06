
def test_modify_group(app):
    if app.group.count() == 0:
        app.group.add(Group(name="test"))
    app.group.modify_first_group()
