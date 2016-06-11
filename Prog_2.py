import mysql.connector
from mysql.connector import errorcode

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
    contactPersonID = input("Enter the ContactPersonID to be deleted")
    #Let's remove a row in contactperson table by specifying the contactPersonID
    deleteContactPerson = "DELETE FROM contactmanagerapplication.contactperson where ContactPersonID = {}".format(contactPersonID)
    cursor.execute(deleteContactPerson)
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