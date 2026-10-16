# KPI Group Project

## Group `<group number>`

- `<student name>` | `<student ID>` | `@<GitHub username>`
- `<student name>` | `<student ID>` | `@<GitHub username>`
- `<student name>` | `<student ID>` | `@<GitHub username>`
- `<student name>` | `<student ID>` | `@<GitHub username>`

Adjust the number of lines to your group size.
Keep student details in your group's private repository.

## Get ready

Use Git to share this working Python project with your group.
Git records changes to files, and GitHub hosts the shared repository online.
The supplied program calculates warehouse key performance indicators (KPIs), such as units processed per hour.

Each student needs a [GitHub account](https://github.com/signup), [GitHub Desktop](https://desktop.github.com/) or another Git client, and Python 3.10 or later.
Sign in using your own account and configure your commit name and email.
Your GitHub-provided private email address is suitable for commits.

## Create the group repository

One group member completes these steps:

1. Open [the project template](https://github.com/brenobeirigo/kpi-group-project) and select **Use this template > Create a new repository**.
   Name it `kpi-group-<number>` and choose **Private**.
2. Fill in the group number in this README and commit the change.
   A commit records changes with a message and an author.
3. Through **Settings > Collaborators**, invite every teammate and the instructor, `brenobeirigo`.
   Share the group repository URL so everyone can accept their invitation.

## Make your own contribution

Every student completes these steps using their own account and computer.
Work in turn so that each student receives the previous student's change.

1. In GitHub Desktop, select **File > Clone repository > URL** and paste your **group repository URL**.
   Cloning creates a local copy on your computer.
2. Open a terminal in the project folder and run `python main.py`.
   On Windows, you can use `py main.py`.
   No additional packages are needed.
3. Select **Fetch origin**, then **Pull origin** if changes are available.
   Pulling brings your teammates' changes to your computer.
   Replace one README placeholder with your own name, student ID, and GitHub username.
4. Review the change, enter a message such as `Add Alex to the group README`, and select **Commit to main**.
   Select **Push origin** to upload your commit.
   Check your entry and commit on GitHub.

If a teammate pushes first, fetch and pull before pushing again.
If Git reports a conflict, resolve the README together so both entries remain, commit the resolution, and push.
Ask the instructor for help if needed.

## Check the completed project

Everyone pulls the final group version and runs `python main.py` again.
The output should be:

```text
Throughput: 30.0 units/hour
Capacity utilization: 75.0 %
Picking accuracy: 95.0 %
```

Confirm that the README identifies every group member, each student has their own contribution commit, and the instructor can access the repository.
On GitHub, open the commit history and select a commit to copy its link.
Keep your own contribution link and agree on the final group commit.
Follow the submission instructions in Canvas.

## Project files

```text
project/
├── kpi/
│   ├── __init__.py
│   └── warehouse.py
├── tests/
│   └── test_warehouse.py
├── main.py
├── requirements.txt
└── README.md
```

`main.py` calls the functions in `kpi/warehouse.py` and prints the results.
The fictional examples use 60 units in 2 hours, output of 18 units against a capacity of 24, and 95 correct orders out of 100.

The supplied code checks are optional for this Git exercise:

```bash
python -m pip install -r requirements.txt
python -m pytest tests/ -q
```
