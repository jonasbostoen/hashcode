from Contributor import Contributor
from Project import Project


def writeSolution(filename, solution: list[tuple[Project, list[Contributor]]]):
    with open(filename, 'w') as file:
        # number of project finished
        file.write(str(len(solution)) + '\n')

        for project, contributors in solution:
            print(contributors)
            # Add solution name
            file.write(project.get_name() + '\n')

            for c in contributors:
                file.write(c.name)
                file.write(' ')
            file.write('\n')


if __name__ == "__main__":
    project = [Project("Test1", 5, 5, 5), Project(
        "Test2", 5, 5, 5), Project("Test3", 5, 5, 5)]
    contributors = [
        Contributor("a"), Contributor("b"), Contributor("c")
    ]
    sol = [
        (project[0], [contributors[0]]),
        (project[1], [contributors[0], contributors[1]]),
        (project[2], contributors)
    ]

    writeSolution("testSolution", sol)
