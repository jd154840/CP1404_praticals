class Project:
    def __init__(self, name: str, start_date: str, priority: int, cost_estimate: float, completion_percent: int):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority

    def __str__(self):
        return f"{self.name}, {self.start_date}, priority:{self.priority}, ${self.cost_estimate}, {self.completion_percent}% done"

    def __repr__(self):
        return str(self)


def testing():
    p1 = Project("Dig", "12/2/27", 1, 13, 50)
    p2 = Project("Fill Hole", "13/2/27", 2, 13, 0)
    projects = [p1, p2]
    projects.sort()
    print(projects)


if __name__ == "__main__":
    testing()
