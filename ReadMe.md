## Team Description Connector

[![Linting](https://github.com/eon-collective/python_project_template/actions/workflows/Python-Linting.yml/badge.svg)](https://github.com/eon-collective/python_project_template/actions/workflows/Python-Linting.yml)

[![Docker Build](https://github.com/eon-collective/python_project_template/actions/workflows/Docker-Build.yml/badge.svg)](https://github.com/eon-collective/python_project_template/actions/workflows/Docker-Build.yml)

[![python_project_template - PyTest](https://github.com/eon-collective/python_project_template/actions/workflows/Testing-CI.yml/badge.svg)](https://github.com/eon-collective/python_project_template/actions/workflows/Testing-CI.yml)


This connector takes employees data and give back a summary of what every one does, number of employees and a count of employees per role.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Usage](#usage)

## Introduction

We realised it could take so long to manually create a summary of what every employee does or even count employees having the same roles. That's the reason as to way we came up with this connector to automatically generate a summary of employees.

The connector requires the following:
- Python
- Docker
- Github
- ECR

## Getting Started

To run this project locally, follow these steps:
1. Clone the repository:

```shell
git clone https://github.com/your-username/your-project.git
```

2. Set up environment:

- Create a virtual environment

```shell
python -m venv myenv
```
- Activate  the environment (windows).
```shell
myenv\Scripts\activate
```
- Activate  the environment (linux).
```shell
source myenv/bin/activate
```
- Install dependancies
```shell
pip install -r requirements.txt
```
2. Set up Docker:

- Docker Build
```shell
docker build -t hello_team:0.0.1 .
```

- Docker run example
```shell
docker run --volume C:\Users\LENOVO\Desktop\EonCollective\adebpt\hello_world:/mnt/input hello_team:0.0.1 --team_ke_json /mnt/input
```
Note, when running, remember to change the paths accordingly.

## Usage

1. If you are running this locally, main.py is the connector entry point, you need to run the the file with `--team_ke_json` argument. For example:

```
python src/main.py --team_ke_json C:\Users\LENOVO\Desktop\EonCollective\adebpt\hello_world
```
`C:\Users\LENOVO\Desktop\EonCollective\adebpt\hello_world` points to a directory having the .json file.

2. If you are running on docker:

```
docker run --volume C:\Users\LENOVO\Desktop\EonCollective\adebpt\hello_world:/mnt/input hello_team:0.0.3 --team_ke_json /mnt/input
```
3. Running test locally
```shell
python -m unittest tests.unit_tests
```
