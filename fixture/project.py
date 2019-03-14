class ProjectHeplper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.20/my_view_page.php")

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def add_project(self, project_name):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector("input[value='%s']" % "Create New Project").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").send_keys(project_name)
        wd.find_element_by_css_selector("input[value='%s']" % "Add Project").click()
        self.open_home_page()

    def get_project_list(self):
        wd = self.app.wd
        project_list = []
        rows = wd.find_elements_by_tag_name("tr")
        for row in rows[2:len(rows)]:
            cells = row.find_elements_by_tag_name("td")
            project = cells[0].text
            project_list.append(project)
        return project_list
