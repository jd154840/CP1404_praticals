"""
Estimated Time: 45 min
Actual Time:
"""

from prac_07.project import Project

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


def display_menu():
    print("- (L)oad Projects")
    print("- (S)ave Projects")
    print("- (D)isplay Projects")
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


main()
