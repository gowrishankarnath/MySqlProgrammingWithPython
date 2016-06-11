import mysql.connector
from mysql.connector import errorcode
from faker import Factory
fake = Factory.create()

config = {
'user': 'root',
'password': 'mysql123',
'host': 'localhost',
'database': 'contactmanagerapplication',
'raise_on_warnings': True,
}

#This is the most efficient way of toggling between the values
import itertools
toggle = itertools.cycle(['Male', 'Female'])
#next(toggle)

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    #Let's insert ten rows to contactperson table
    for person in range(1,11):
        contactPersonID = person
        firstName = fake.first_name_male() #generate fake first name
        lastName = fake.last_name_male() #generate fake middle name
        middleName = fake.last_name_male() #generate fake last name
        dateOfBirth = fake.date() #generate fake DOB
        contactPersonType = next(toggle)

        #In SQL statement the values need to be enclosed within double quotes
        #I'm providing the same by explicity specifying double quotes and removing it's special meaning
        addContactPerson = "INSERT INTO contactmanagerapplication.contactperson(" \
                           "ContactPersonID, FirstName, MiddleName, LastName, DateOfBirth," \
                           "ContactPersonType)VALUES({},\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".\
            format(contactPersonID,firstName,lastName,middleName,dateOfBirth,contactPersonType)
        cursor.execute(addContactPerson)
        cnx.commit()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor.close()
    cnx.close()

