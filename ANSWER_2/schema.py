import sqlite3
import os

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "college.db"
DBPATH = os.path.join(DIRPATH, DBFILENAME)

def schema(DBPATH):
    with sqlite3.connect(DBPATH) as conn:
        cur = conn.cursor()

        SQL = "DROP TABLE IF EXISTS campuses;"
        cur.execute(SQL)

        SQL = """CREATE TABLE campuses(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            city VARCHAR(128),
            state VARCHAR (128)
            );"""
        cur.execute(SQL)

        SQL = "DROP TABLE IF EXISTS students;"
        cur.execute(SQL)

        SQL = """CREATE TABLE students(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(128),
            last_name VACHAR(128),
            gpa FLOAT, 
            campus_pk INTERGER (128),
            FOREIGN KEY (campus_pk) REFERENCES campuses(pk)
            );"""
        cur.execute(SQL)


if __name__ == "__main__":
    schema(DBPATH)