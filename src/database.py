"""
File name: database.py
Description: Functions for connecting to database, and executing SQL statements.
"""
import logging
import sqlite3

DATABASE = "data/SOAP.db"

def get_connection():
    """
    Tries to open a connection to the database and return it. 
    Logs and re-raises errors.
    """
    try:
        return sqlite3.connect(DATABASE)
    except sqlite3.Error as e:
        logging.error(f"Database connection failed at {DATABASE}: {e}")
        raise


def run_db_operation(statement):
    """
    Connects to database, executes SQL, logs / re-raises errors, closes connection.
    - statement is a possibly invalid SQL statement string
    """
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(statement)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        rows = "go"
        input("Press enter to continue.\n>> ")
        conn.commit()
    
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        raise

    finally:
        if conn:
            conn.close()



