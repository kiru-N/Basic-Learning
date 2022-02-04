import mysql.connector
from tabulate import tabulate

sql_connect = mysql.connector.connect(host="localhost", user='root', password="Nevin123", database='my_db')


def insert_data(name, age, city):
    res = sql_connect.cursor()
    qry = "insert into users (Name,Age,City) values (%s,%s,%s)"
    res.execute(qry, (name, age, city))
    sql_connect.commit()


def update_data(name, age, city, id):
    res = sql_connect.cursor()
    qry = 'Update users set Name=%s, Age=%s, City=%s where id=%s'
    res.execute(qry, (name, age, city, id))
    sql_connect.commit()


def select_data():
    res = sql_connect.cursor()
    qry = 'select ID,Name,Age,City from users'
    res.execute(qry)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", 'Name', 'Age', 'City']))



def delete_data(id):
    res = sql_connect.cursor()
    qry = 'delete from users where id=%s'
    res.execute(qry, (id,))
    sql_connect.commit()


show_message = '''
1. Insert Data
2. Update Data
3. Select data
4. Delete
5. Exit
'''

while True:
    print(show_message)
    choice = int(input('Enter your choice: '))
    if choice == 1:
        name, age, city = input('Enter all the details: ').split(',')
        insert_data(name, age, city)
        print("Inserted data successfully")
    elif choice == 2:
        name, age, city, id = input('Enter all the details: ').split(',')
        update_data(name, age, city, id)
        print("Updated data successfully")
    elif choice == 3:
        select_data()
    elif choice == 4:
        id = input('Enter the ID: ')
        delete_data(id)
        print('Data delete success')
    elif choice == 5:
        quit()
    else:
        print('Enter the valid choice. Try again')