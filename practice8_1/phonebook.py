import psycopg2
from connect import connect

def search(pattern):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()


def paginate(limit, offset):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_phonebook_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()


def upsert(name, phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL upsert_user(%s, %s)", (name, phone))
    conn.commit()

    conn.close()


def delete(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s)", (value,))
    conn.commit()

    conn.close()