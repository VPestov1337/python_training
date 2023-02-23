from model.group import Group
from timeit import timeit

def test_group_list(app, db):
    print(timeit(lambda:  app.group.get_groups_list(), number=1000))
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    print(timeit(lambda: map(clean, db.get_groups_list()), number=1000))
