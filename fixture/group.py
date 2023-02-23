from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()

    def add(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_fields(group)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def fill_group_fields(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def modify_first_group(self, group):
        self.modify_group_by_index(group, 0)

    def modify_group_by_index(self, group, index):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_name("edit").click()
        self.fill_group_fields(group)
        wd.find_element_by_name("update").click()
        self.group_cache = None

    def modify_group_by_id(self, group, id):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_name("edit").click()
        self.fill_group_fields(group)
        wd.find_element_by_name("update").click()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_groups_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for el in wd.find_elements_by_css_selector("span.group"):
                text = el.text
                gr_id = el.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=gr_id))
        return list(self.group_cache)
