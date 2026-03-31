import csv
from connect import get_connection

def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row['name'], row['phone'])
            )

    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

def update_contact(old_name):
    conn = get_connection()
    cur = conn.cursor()

    new_name = input("New name (or press enter to skip): ")
    new_phone = input("New phone (or press enter to skip): ")

    if new_name:
        cur.execute(
            "UPDATE phonebook SET name = %s WHERE name = %s",
            (new_name, old_name)
        )

    if new_phone:
        cur.execute(
            "UPDATE phonebook SET phone = %s WHERE name = %s",
            (new_phone, old_name)
        )

    conn.commit()
    cur.close()
    conn.close()

def query_contacts():
    conn = get_connection()
    cur = conn.cursor()

    choice = input("Search by (1-name / 2-phone prefix): ")

    if choice == '1':
        name = input("Enter name: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE name ILIKE %s",
            ('%' + name + '%',)
        )
    elif choice == '2':
        prefix = input("Enter phone prefix: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE phone LIKE %s",
            (prefix + '%',)
        )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

def delete_contact():
    conn = get_connection()
    cur = conn.cursor()

    value = input("Enter name or phone to delete: ")

    cur.execute(
        "DELETE FROM phonebook WHERE name = %s OR phone = %s",
        (value, value)
    )

    conn.commit()
    cur.close()
    conn.close()

def menu():
    while True:
        print("\n1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == '1':
            insert_from_csv("contacts.csv")
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            name = input("Enter name to update: ")
            update_contact(name)
        elif choice == '4':
            query_contacts()
        elif choice == '5':
            delete_contact()
        elif choice == '0':
            break

if __name__ == "__main__":
    menu()