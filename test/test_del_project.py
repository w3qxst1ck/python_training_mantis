import random

def test_delete_project(app):
    app.session.login("administrator", "root")
    # old_projects = app.project.get_project_list()
    # deleting_project = random.choice(old_projects)
    app.project.delete_project("Xmut")
    # new_projects = app.project.get_project_list()
    # old_projects.remove(deleting_project)
    # assert sorted(new_projects) == sorted(old_projects)