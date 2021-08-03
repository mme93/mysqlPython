import mysql.connector

db = mysql.connector.connect(
    host="212.227.165.166",
    user="mameie",
    passwd="!Mameie93",
    database="kfzOptimizer"
    )

mycursor=db.cursor()

mycursor.execute("SELECT * FROM Benutzer")

for x in mycursor:
    print(x)
