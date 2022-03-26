class Project:
    def __init__(self, name, duration, score, best_before):
        self.name = name
        self.duration = duration
        self.score = score
        self.best_before = best_before
        self.required_skills: list[tuple[str, int]] = []

    def add_required_skill(self, skill):
        self.required_skills.append(skill)

    def set_required_skills(self, skills):
        self.required_skills = skills

    def set_name(self, name):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def get_contributors(self):
        return self.requiredContributors

    def get_true_score(self, day: int) -> int:
        if day < self.best_before:
            return self.score
        else:
            true_score = self.score - (day + 1 - self.best_before)
        return true_score if true_score >= 0 else 0

    def __repr__(self) -> str:
        return f'{self.name}, duration: {self.duration}, score: {self.score}, best_before: {self.best_before}, skills: {self.required_skills}'
