import json
import os

def read_data(path):
    filename = "teamke.json"
    full_path = os.path.join(path, filename)
    with open(full_path, 'r') as file:
        data = json.load(file)
    return data

def introduce_team(data):
    team_size = len(data)

    print()
    print("The size of our Kenyan team is:", team_size)
    print()
    role_groups = {}
    for person in data:
        role = person['Role']
        if role in role_groups:
            role_groups[role].append(person['Name'])
        else:
            role_groups[role] = [person['Name']]

    # Print the grouped data
    for role, people in role_groups.items():
        print(f'Role: {role}, People: {len(people)}')

def give_details(data):
    print()
    for record in data:
        print(f'We have {record["Name"]} who works as {record["Role"]}.')
