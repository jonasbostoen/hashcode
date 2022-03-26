from Project import Project
from Contributor import Contributor

# return list of all incresed skills when certain project is completed


def increase_skill(project: Project, project_contributors: list[Contributor]):
    #print(len(project.required_skills), len(project_contributors))
    assert(len(project.required_skills) == len(project_contributors))
    score_increase_skill = []
    for i, contributor in enumerate(project_contributors):
        req_skill, req_level = project.required_skills[i]
        skill_level = contributor.skills[req_skill]
        for skill, level in contributor.skills.items():
            if (req_skill != skill):
                continue
            if level <= req_level:
                # increase skill
                score_increase_skill.append((contributor, skill, 1))

    return score_increase_skill
