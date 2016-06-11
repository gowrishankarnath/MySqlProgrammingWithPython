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
    #Let's read all the rows in the table
    readContactPerson = "select * from contactmanagerapplication.contactperson"
    cursor.execute(readContactPerson)
    #specify the attributes that you want to display
    for (contactPersonID, firstName, lastName, middleName, dateOfBirth,contactPersonType ) in cursor:
        print("{}, {}, {}, {}, {}, {}".format(contactPersonID,firstName,middleName,lastName,dateOfBirth,contactPersonID))
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