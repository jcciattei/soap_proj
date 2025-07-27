"""
File name: database.py
Description: Functions for connecting to database, insertion, selection, and deletion.
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


def _run_db_operation(sql, params=(), commit=False, result_fn=None):
    """
    Connects to database, executes SQL, logs / re-raises errors, closes connection.
    - sql: SQL statement with "?" placeholders
    - params: tuple of bind-params
    - commit: bool of whether to commit
    - result_fn: optional fn(cursor) as return value
    """
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(sql,params)

        if commit:
            conn.commit()

        if result_fn:
            return result_fn(cur)
    
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        raise

    finally:
        if conn:
            conn.close()


def insert_customer_agency(agency_id, name, address, city, phone_number):
    """
    Attempts to insert an agency record with attributes from user input.
    """
    return _run_db_operation(
        """
        INSERT INTO customer_agency(agency_id, name, address, city, phone_number)
        VALUES (?, ?, ?, ?, ?)
        """,
        (agency_id, name, address, city, phone_number),
        commit=True,
        result_fn=lambda cur: cur.lastrowid
    )


