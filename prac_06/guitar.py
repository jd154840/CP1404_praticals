from datetime import datetime

CURRENT_YEAR = 2026


class Guitar:
    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        guitar_age = CURRENT_YEAR - self.year
        return guitar_age

    def is_vintage(self):
        if CURRENT_YEAR - self.year > 50:
            return True
        else:
            return False
