# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.add(Group(name="Test", header="Test head", footer="Test footer"))


def test_add_group_empty(app):
    app.group.add(Group(name="", header="", footer=""))



def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group()
    app.session.logout()

