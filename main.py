import mysql.connector as ms

try:
    mycon = ms.connect(
        host="localhost",
        user="root",
        password="Your SQL Database Password",
        database="Your Database Name",
        port=3306
    )

    if mycon.is_connected():
        print("Connected Successfully")

        mycursor = mycon.cursor()

        # Correct table name
        mycursor.execute("SELECT * FROM Name")

        mydata = mycursor.fetchall()

        for row in mydata:
            print(row)

except ms.Error as err:
    print("Error:", err)
