"""
Estimated Time: 40
Actual Time: At least 40
"""

# get user emails until email is blank
# get the name associated with email using string methods
# store email: name into a dictionary
# check if name is correct
def main():
    email = input("Email: ")
    emails = []
    email_to_name = {}

    while email != "":
        emails.append(email)
        email = input("Email: ")

    for email in emails:
        name = name_from_email(email)
        email_to_name[email] = email_to_name.get(email, name)
        print(f"{email}: {name}")



def name_from_email(email):
    username = email.split("@")[0]
    name = username.title()
    return name

main()