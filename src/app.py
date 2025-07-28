"""
File name: app.py
Description: Driver program for interacting with SOAP database.
"""
from database import run_db_operation

PROMPT = "Enter valid SQL statement or 'quit' to exit the application.\n>> "

def prompt_user():
    """Enable user to enter SQL statements to insert, delete, or search the database"""
    statement = "select * from customer_agency"
    while statement != "quit":
        statement = input(PROMPT)
        if statement != "quit":
            run_db_operation(statement)
        else:
            print("Quitting application")

if __name__ == "__main__":
    prompt_user()

        