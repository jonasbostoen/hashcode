from main import contributors, projects

projects.sort(key=lambda x: x.best_before)
print(projects)
