import mysql.connector
from mysql.connector import errorcode

#Mysql Connector
def connection():
    try:
        db = mysql.connector.connect(
            host="bxaflyxymmraktyokfkw-mysql.services.clever-cloud.com",
            user="ualt4ntcrqhhmrcf",
            password="ZiHQOl1PhFJ1RQjQw4xM",
            database="bxaflyxymmraktyokfkw"
        )
        print("Connection successful")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        db.close()

def main():
    #New connection
    connection()

if __name__ == "__main__":
    main()