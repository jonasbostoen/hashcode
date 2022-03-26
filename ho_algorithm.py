from Project import Project
from Contributor import Contributor
from parsing import parse
from increaseSkill import increase_skill
from writeSolution import writeSolution
from collections import defaultdict
import sys

input_file_name = sys.argv[1]
with open(input_file_name) as file:
    input_text = file.read()

contributors_in, remaining_projects = parse(input_text)


def get_next_best_project(day: int, remaining_projects: list[Project]):
    # select best project (according to some heuristic)
    # score proposal: return project[1]/(project[3]+project[0])
    # Earliest deadline first with heighest weight (= score/number_of_days) and availability
    # for p in remaining_projects[0:5]:
    p = sorted(remaining_projects, key=lambda x: (
        get_project_weight_v1(x)), reverse=True)
    return p


def get_project_weight_v1(project: Project):
    return project.score/project.duration


def get_project_weight_v2(project: Project):
    return project.score / (project.duration + len(project.required_skills))


def get_project_weight_by_nb_of_contributors(project: Project):
    return len(project.required_skills)


def get_project_availability(project: Project, day: int):
    # check mean level difference
    # score: int
    # c: Contributor
    # for c in get_best_contributors_for_project(day, project):
    #   score +=
    # check not null
    return bool(get_best_contributors_for_project(day, project))


def get_best_contributors_for_project(day: int, project: Project) -> list[tuple[Contributor, str, int]]:
    global contributors_in
    for skill_name, skill_level in project.required_skills:
        contributors_in = list(filter(lambda x: (x.is_available(
            day), x.skills[skill_name] - skill_level >= -1), contributors_in))
        if len(contributors_in) == 0:
            return None

        contributors_in.sort(key=lambda x: (x.skills[skill_name]))

        # result = list(filter(lambda x: (x % 13 == 0), my_list))
    # Which skill will they work on tuple(Contributor, skill_name)
    best_contributors = []
    assigned_contributors = []

    for c in contributors_in:
        # not available at this day
        if c.available_from_day > day:
            continue

        # nog niet goed, pakt gewoon de eerste de beste
        for (r_skill_name, rlevel) in project.required_skills:
            level = c.skills[r_skill_name]
            if level >= rlevel:
                if c.name not in assigned_contributors:
                    best_contributors.append((c, skill_name))
                    assigned_contributors.append(c.name)

    return best_contributors if len(best_contributors) == len(project.required_skills) else None


day: int = 0
projects_and_contributors_per_day = defaultdict(list)

remaining_projects.sort(key=lambda x: (x.best_before, -x.score), reverse=True)

score_increases_per_day: dict[int,
                              list[tuple[Contributor, str, int]]] = defaultdict(list)
output: list[tuple[Project, list[Contributor]]] = []
while True:
    print(day)
    # every day, increase the skill levels for the projects that are finished
    skill_level_increases_for_current_day = score_increases_per_day[day] or [
    ]
    # TODO: fix skill => Maarten: should be fixed
    for contributor, skill_name, increase in skill_level_increases_for_current_day:
        contributor.skills[skill_name] += increase

    next_best_projects = get_next_best_project(day, remaining_projects)
    if day > 200000:
        break
    next_best_project = None
    project_contributors = None
    for trying_next_best_project in next_best_projects:
        project_contributors = get_best_contributors_for_project(
            day, trying_next_best_project)

        if project_contributors is None:
            continue
        print('get_best_contributors_for_project out', len(
            project_contributors), len(trying_next_best_project.required_skills))
        next_best_project = trying_next_best_project
        break

    if next_best_project is None:
        if len(projects_and_contributors_per_day[day] or []) == 0:
            break
        day += 1
        continue
    remaining_projects.remove(next_best_project)
    if project_contributors is None:
        continue
    trying_next_best_project = next_best_project
    project_contributors_sorted: list[Contributor] = []
    for contributor, skill_name in project_contributors:
        project_contributors_sorted.append(contributor)
    # project_contributors_sorted: list[Contributor] = []
    # for required_skill_name, required_skill_score in next_best_project.required_skills:
    #     for contributor, skill_name in project_contributors:
    #         if skill_name == required_skill_name:
    #             project_contributors_sorted.append(contributor)
    #             break

    output.append((next_best_project, project_contributors_sorted))
    for duration_day in range(0, next_best_project.duration):
        # reserve this project for the upcoming days
        if projects_and_contributors_per_day[day +
                                             duration_day] is None:
            projects_and_contributors_per_day[day +
                                              duration_day] = []
        projects_and_contributors_per_day[day +
                                          duration_day].append((next_best_project, project_contributors_sorted))
    # update availability
    for contributor in project_contributors_sorted:
        contributor.available_from_day = day + next_best_project.duration
    # initialize this with a list:
    # TODO: day + duration + 1 or + 0?
    if score_increases_per_day[day + next_best_project.duration] is None:
        score_increases_per_day[day +
                                next_best_project.duration] = []
    skill_level_increases_for_last_day = score_increases_per_day[day +
                                                                 next_best_project.duration]
    # TODO: not every contributor increases in skill, check this => Maarten= checked in increase_skill
    levelincreases = increase_skill(
        next_best_project, project_contributors_sorted)
    for temp in levelincreases:
        skill_level_increases_for_last_day.append(
            temp)  # (contributor, skill_name, 1)
    score_increases_per_day[day +
                            next_best_project.duration] = skill_level_increases_for_last_day

writeSolution(sys.argv[2], output)
