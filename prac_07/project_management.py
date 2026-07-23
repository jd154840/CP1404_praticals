"""
Estimated Time: 45 min
Actual Time: Ages
"""

from prac_07.project import Project
import datetime

FILENAME = "projects.txt"


def main():
    projects = load_projects()
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    display_menu()
    user_input = input(">> ").upper()
    while user_input != "Q":
        if user_input == "L":
            projects = load_projects()
            display_menu()
            user_input = input(">> ").upper()
        if user_input == "S":
            save_projects(projects)
            display_menu()
            user_input = input(">> ").upper()
        if user_input == "D":
            display_projects(projects)
            display_menu()
            user_input = input(">> ").upper()
        if user_input == "F":
            print(filter_by_date(projects))
            display_menu()
            user_input = input(">> ").upper()
        if user_input == "U":
            update_project(projects)
            display_menu()
            user_input = input(">> ").upper()
        if user_input == "A":
            add_project(projects)
            display_menu()
            user_input = input(">> ").upper()


def display_menu():
    print("- (L)oad Projects")
    print("- (S)ave Projects")
    print("- (D)isplay Projects")
    print("- (F)ilter Projects by Date")
    print("- (A)dd New Project")
    print("- (U)pdate Project")
    print("- (Q)uit")


def display_projects(data):
    data.sort()
    print("Completed Projects:")
    for project in data:
        if project.completion_percent == 100:
            print(project)
    print("Incomplete Projects:")
    for project in data:
        if project.completion_percent < 100:
            print(project)


def load_projects():
    with open(FILENAME, 'r') as in_file:
        in_file.readline()
        projects = []
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    in_file.close()
    return projects


def save_projects(data):
    filename = input("Save to File: ")
    with open(filename, 'w') as out_file:
        for line in data:
            print(line, file=out_file)
    out_file.close()


def filter_by_date(data):
    user_date = input("Select a date: ")
    user_dmy = user_date.split('/')
    user_date_formatted = datetime.date(int(user_dmy[2]), int(user_dmy[1]), int(user_dmy[0]))
    print(f"Projects to be completed after {user_date}:")
    for project in data:
        date = project.start_date.split('/')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        unpacked_date = datetime.date(year, month, day)
        if user_date_formatted < unpacked_date:
            print(project)
    return user_date_formatted


def update_project(data):
    for i, project in enumerate(data):
        print(f"{i + 1} {project}")
    user_input = int(input("Select Project Index to modify: "))
    print(data[user_input - 1])
    new_percentage = int(input("New Percentage: "))
    data[user_input - 1].completion_percent = new_percentage
    new_priority = int(input("New Priority: "))
    data[user_input - 1].priority = new_priority
    pass


def add_project(data):
    project_name = input("Name: ")
    project_date = input("Date: ")
    project_priority = int(input("Priority: "))
    project_price = int(input("Price: "))
    project_completion = int(input("Completion %: "))
    data.append(Project(project_name, project_date, project_priority, project_price, project_completion))


main()
