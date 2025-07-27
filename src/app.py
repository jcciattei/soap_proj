"""
File name: app.py
Description: Driver program for interacting with SOAP database.
"""
from database import insert_customer_agency

PROMPT = "Available commands are:\ni\tinsert\ns\tselect\nd\tdelete\nq\tquit\n>>\t"
RECORD_TYPE = """Select record type:\nc\tcustomer agency\no\toffice
r\trental agreement\np\tparty to (link customer agency to rental agreement)
m\tmanages (link office to rental agreement)\n>>\t"""


def prompt_insert():
    """Enable user to decide which record type to insert"""
    user_input = input(f"Insertion operation. {RECORD_TYPE}").strip().lower()
    if user_input == 'c':
        fields = ["agency_id", "name", "address", "city", "phone_number"]
        attribute_data = {}
        for field in fields:
            attribute_data[field] = input(f"Enter {field}: ")
        insert_customer_agency(**attribute_data)
    elif user_input == 'o':
        pass
    elif user_input == "r":
        pass
    elif user_input == "p":
        pass
    elif user_input == "m":
        pass
    else:
        print("Incorrect selection: Try c, o, r, p, or m. Returning to main menu.")
        

def prompt_select():
    pass


def prompt_delete():
    pass


def prompt_user():
    """Enable user to select options: insert, select, delete, quit"""
    prompt = True
    while prompt:
        user_input = input(PROMPT).strip().lower()
        if user_input == 'i':
            prompt_insert()
        elif user_input == 's':
            prompt_select()
        elif user_input == "d":
            prompt_delete()
        elif user_input == "q":
            print("Quitting application")
            prompt = False
        else:
            print("Incorrect selection: Try i, s, d, or q.")


if __name__ == "__main__":
    prompt_user()

        