"""This script contain modular function to process employees details."""

import json
import os


def read_data(path):
    """Read JSON data from a file located at the specified path.

    Args:
        path (str): The directory path where the JSON file is located.

    Returns:
        dict: A Python dictionary containing the parsed JSON data from the file.
    """
    filename = "teamke.json"
    full_path = os.path.join(path, filename)
    with open(full_path, "r") as file:
        data = json.load(file)
    return data


def introduce_team(data):
    """Display team size and role distribution.

    Args:
        data (list of dict): List of dictionaries with "Name" and "Role" keys.

    Returns:
        dict: Role-based team members.
    """
    team_size = len(data)

    print()
    print("The size of our Kenyan team is:", team_size)
    print()
    role_groups = {}
    for person in data:
        role = person["Role"]
        if role in role_groups:
            role_groups[role].append(person["Name"])
        else:
            role_groups[role] = [person["Name"]]

    for role, people in role_groups.items():
        print(f"Role: {role}, People: {len(people)}")

    return role_groups


def give_details(data):
    """Print details of team members and their roles.

    Args:
        data (list of dict): List of dictionaries with "Name" and "Role" keys.
    """
    print()
    for record in data:
        print(f'{record["Name"]} works as {record["Role"]}.')

    return
