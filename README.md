# KPI Group Project

## Group `<group number>`

- `<student name>` | `<student ID>` | `@<GitHub username>`
- `<student name>` | `<student ID>` | `@<GitHub username>`
- `<student name>` | `<student ID>` | `@<GitHub username>`
- `<student name>` | `<student ID>` | `@<GitHub username>`

Each student replaces one line and commits their own change.
Adjust the number of lines to your group size.
Fill in student IDs only in your group's private repository.

## What you will practice

Git records changes to a project's files.
GitHub hosts the shared project online in a repository.
A commit records a set of changes with a message and an author.

Your group will share a working Python project that calculates warehouse key performance indicators (KPIs).
A KPI is a number used to describe performance, such as units processed per hour.
The Python code is supplied and ready to run.
Your task is to clone the project, add your own details to the README, and share that change with your group.

## Prepare your account

1. Create a [GitHub account](https://github.com/signup) if you do not have one.
2. Install [GitHub Desktop](https://desktop.github.com/) or use another Git client you already know.
   Sign in using your own account and configure your commit name and email.
   You can use your GitHub-provided private email address.
3. Check that Python 3.10 or later is available on your computer.

## Create one repository for your group

1. Choose one group member to open [the project template](https://github.com/brenobeirigo/kpi-module-template-v2).
   Select **Use this template > Create a new repository**.
2. Name it `kpi-group-<number>` and choose **Private**.
   Use one repository for the whole group.
3. The owner fills in the group number in this README and commits that change.
   Through **Settings > Collaborators**, invite every teammate and the instructor, `brenobeirigo`.
   Everyone accepts their invitation.

## Each student clones and runs the project

Cloning creates a copy of the shared repository on your computer.
Every student completes these steps using their own computer and account.

1. In GitHub Desktop, select **File > Clone repository > URL**.
   Paste your **group repository URL**, choose a local folder, and clone it.
2. Open a terminal in the project folder and run:

```bash
python main.py
```

On Windows, you can use `py main.py`.
No additional Python packages are needed to run the program.
The output should be:

```text
Throughput: 30.0 units/hour
Capacity utilization: 75.0 %
Picking accuracy: 95.0 %
```

`main.py` calls functions in `kpi/warehouse.py` and prints their results.
The fictional examples calculate 60 units divided by 2 hours, 18 units divided by a capacity of 24, and 95 correctly picked orders out of 100.
The last two ratios are multiplied by 100 to give percentages.

The project is organized as follows:

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

## Each student commits and pushes their name

Work in turn so that each student can receive the previous student's change.

1. In GitHub Desktop, select **Fetch origin**, then **Pull origin** if changes are available.
   Pulling brings your teammates' changes to your computer.
2. Open `README.md` in your editor and replace one placeholder with your own name, student ID, and GitHub username.
   Keep the entries already added by your teammates.
3. Review the change in GitHub Desktop.
   Enter a message such as `Add Alex to the group README`, then select **Commit to main**.
4. Select **Push origin** to upload your commit.
   Open the group repository on GitHub and check that your entry appears in the README and that your commit appears in its history.

If a teammate pushes first, fetch and pull before pushing again.
If Git reports a conflict, resolve the README together so that both entries remain.
Save the file, commit the resolution, and push.
Ask the instructor for help if you are unsure how to resolve it.

## Finish together

- Check that the README contains the group number and every group member's details.
- Check that each student has their own commit adding their entry.
- Everyone pulls the completed README and runs `python main.py` again.
- Confirm that the instructor can access the repository, and record the final group commit link.

On GitHub, open the commit history and select a commit to copy its link.
Each student keeps the link to their own contribution.
Keep the repository private when it contains student IDs or course data.

## Supplied code checks

The `tests/` folder contains checks for the supplied KPI functions.
You can run them with:

```bash
python -m pip install -r requirements.txt
python -m pytest tests/ -q
```

Writing new functions or new tests is not required for this Git exercise.
