import mysql.connector
def mysqlfn(self):

    mydb = mysql.connector.connect(
    host="localhost",
    user="idodo",
    passwd="idodo123",
    database="image"
    )
    mycursor = mydb.cursor(buffered=True)
    