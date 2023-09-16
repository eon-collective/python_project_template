"""This is the main code entry point."""

import argparse

from modules.process_team_summary import introduce_team  # D
from modules.process_team_summary import give_details, read_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a summary for team kenya.")

    parser.add_argument("--team_ke_json", type=str, help="json path")
    args = parser.parse_args()
    team_ke_json = args.team_ke_json

    employees_data = read_data(team_ke_json)
    introduce_team(employees_data)
    give_details(employees_data)
