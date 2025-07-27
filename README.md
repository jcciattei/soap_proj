## CMSC461-Proj: SOAP database and application

This application provides an interface for inserting, selecting and deleting from the 

System for Occupancy Agreement (SOAP).

## Prerequisites

1. Latest version of sqlite3 application installed and available on PATH

2. Python interpreter

2. Ability to install and use git for the command line steps

## Initial Setup

1. Clone the git repository and navigate to the root directory.
```bash
git clone https://github.com/ddddddd

```

2. Install virtual environment for Python (if not already installed).
```bash
pip install virtualenv
```

3. Create a virtual environment
```bash
virtualenv env
```

4. Activate the virtual environment (Windows)
```bash
env\Scripts\activate
```

OR Activate the virtual environment (mac/Linux)
```bash
source planner-env/bin/activate
```

5. Install dependencies
```bash
pip install -r requirements.txt
```

6. Navigate to the src data directory and initialize the database.
```bash
sqlite3 SOAP.db < SOAP_schema.sql
```

## Running the application
From the root directory, run the command
```bash
python app.py
```

## Additional information

- Any time new dependencies are added to the python files, run this command

in the root directory to update the requirements.txt file.
```bash
pip freeze > requirements.txt
```

## Troubleshooting



## Contact

For questions or contributions, please contact: 






