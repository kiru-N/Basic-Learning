class AddressBook:
    def __init__(self):
        self.name = ''
        self.emailid = ''

    def GetContactDetails(self):
        self.name = input('Name: ')
        self.emailid = input('EmailID: ')
        return self.name, self.emailid



connection = sqlite3.connect("C:\\Users\\NEVIN\\Desktop\\DB\\Test.db")
cursor = connection.cursor()
connection.execute('Drop table ContactList')
sql_command = '''Create table ContactList (
                ID integer Not null,
                Name Text Not Null,
                email_id Text unique Not NUll,
                primary key(ID))
                '''
cursor.execute(sql_command)

choice = True
while choice:
    show = ''' 
            1.Add new Contact  
            2.Update contact
            3.Delete Contact
            4.Display contact
            5.Exit
            '''
    print(show)
    choice = int(input('Enter your choice: '))
    if choice == 1:
        contact = AddressBook()
        (name,emailid) = contact.GetContactDetails()
        sql_command = '''Insert into contactList(name,email_id)
                        values(?,?)
                        '''
        cursor.execute(sql_command,(name,emailid))
        connection.commit()

    elif choice == 2:
        pass
    elif choice == 4:
        cursor.execute('Select * from ContactList')
        result = cursor.fetchall()
        print(result)
    elif choice == 5:
        connection.close()
        break
    else:
        print('Please select the valid choice')
