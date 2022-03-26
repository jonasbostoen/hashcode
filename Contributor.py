from collections import defaultdict


class Contributor:
    def __init__(self, name):
        self.name = name
        self.skills: dict[str, int] = defaultdict(int)
        self.available_from_day = 0

    def add_skill(self, skill):
        self.skills.append(skill)

    def set_skills(self, new_skills):
        self.skills = new_skills

    def is_available(self, day: int) -> bool:
        return self.available_from_day >= day

    def __repr__(self) -> str:
        return f'{self.name}, skills: {self.skills}, available_from: {self.available_from_day}'
