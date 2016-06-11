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

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    contactPersonID = input('Enter the Contact Person ID whose records needs to be updated')
    firstName = fake.first_name_male() #generate fake first name
    #Let's update a row in contactperson table by specifying the contactPersonID
    updateContactPerson = "UPDATE contactmanagerapplication.contactperson SET FirstName = \"{}\" WHERE ContactPersonID = {}".format(firstName, contactPersonID)
    cursor.execute(updateContactPerson)
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