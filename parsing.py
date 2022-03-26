from Contributor import Contributor
from Project import Project
from collections import defaultdict


def parse(input_text: str):
    split_input = input_text.split("\n")
    nb_contributors = int(split_input[0].split(' ')[0])
    nb_projects = int(split_input[0].split(' ')[1])

    # parsing for contributors
    contributors: list[Contributor] = []
    nb_contributors_to_process = nb_contributors
    input_index = 1
    while nb_contributors_to_process > 0:
        contributor_info = split_input[input_index]
        contributor_name = contributor_info.split(' ')[0]
        nb_of_skills = int(contributor_info.split(' ')[1])
        new_contributor = Contributor(contributor_name)
        new_skills = defaultdict(int)

        for i in range(nb_of_skills):
            skill_input = split_input[input_index + i + 1]
            skill_name = skill_input.split(" ")[0]
            skill_level = int(skill_input.split(" ")[1])
            new_skills[skill_name] = skill_level
        new_contributor.set_skills(new_skills)
        input_index += nb_of_skills + 1
        contributors += [new_contributor]
        nb_contributors_to_process -= 1

    # parsing for projects
    projects: list[Project] = []
    nb_projects_to_process = nb_projects
    while nb_projects_to_process > 0:
        project_info = split_input[input_index]
        print(project_info)
        split_project_info = project_info.split(' ')
        project_name = split_project_info[0]
        project_duration = int(split_project_info[1])
        project_score = int(split_project_info[2])
        project_best_before = int(split_project_info[3])
        project_nb_of_roles = int(split_project_info[4])

        new_project = Project(project_name, project_duration,
                              project_score, project_best_before)
        required_skills = []
        for i in range(project_nb_of_roles):
            input_skill = split_input[input_index + i + 1]
            skill_name = input_skill.split(' ')[0]
            skill_level = int(input_skill.split(' ')[1])
            required_skills += [(skill_name, skill_level)]
        new_project.set_required_skills(required_skills)
        projects += [new_project]
        input_index += project_nb_of_roles + 1
        nb_projects_to_process -= 1
    return contributors, projects
