# -*- coding: utf-8 -*-
import time

from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.add(Group(name="Test", header="Test head", footer="Test footer"))
    app.session.logout()


def test_add_group_empty(app):
    app.session.login(username="admin", password="secret")
    app.group.add(Group(name="", header="", footer=""))
    app.session.logout()


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group()
    app.session.logout()
