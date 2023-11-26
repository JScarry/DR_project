import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  #user="datarep",  # this is the user name on my mac
  #passwd="password" # for my mac
  database="car_DB1"
)

cursor = db.cursor()
sql="CREATE TABLE car (id INT AUTO_INCREMENT PRIMARY KEY, Make VARCHAR(50), Model VARCHAR(50), Registration VARCHAR(50), Price INT)"

cursor.execute(sql)

db.close()
cursor.close()