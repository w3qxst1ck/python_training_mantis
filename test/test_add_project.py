import string
import random


def test_add_project(app):
    symbols = string.digits + string.ascii_letters
    new_project_name = "".join([random.choice(symbols) for i in range(random.randrange(10))])
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    app.project.add_project(new_project_name)
    new_projects = app.project.get_project_list()
    old_projects.append(new_project_name)
    # assert sorted(old_projects) == sorted(new_projects)
