import sqlite3

db_connect = sqlite3.connect('C:\\Users\\NEVIN\\Desktop\\DB\\users.db')

screen = '''
    1. Select
    2. Insert
    3. Delete
    4. Update
'''
print(screen)


def select_data():
    qry = 'select * from users'
    result = db_connect.execute(qry)
    for records in result:
        print(records)


def insert_data(name, age, city):
    qry = "insert into users (NAME,AGE,CITY) values (?,?,?)"
    db_connect.execute(qry, (name, age, city))
    db_connect.commit()
    print('data inserted successfully')


def update_data(name, age, city, id):
    qry = "update users set NAME = ?, AGE = ? ,CITY = ? where ID = ?"
    db_connect.execute(qry, (name, age, city, id))
    db_connect.commit()
    print('data updated successfully')


def delete_data(id):
    qry = "delete from users where ID = ?"
    db_connect.execute(qry, id)
    db_connect.commit()
    print('data deleted successfully')


cont = 'y'

while cont == 'y':
    choice = int(input('Enter your choice: '))
    if choice == 1:
        select_data()
    elif choice == 2:
        name, age, city = input('Enter all details: ').split()
        insert_data(name, age, city)
    elif choice == 3:
        id = input('Enter id: ')
        delete_data(id)
    elif choice == 4:
        id, name, age, city = input('Enter all details: ').split()
        update_data(name, age, city, id)
    else:
        print('Enter valid choice(1~4)')

    cont = input("Enter 'y' to continue ")

print('Thank you')