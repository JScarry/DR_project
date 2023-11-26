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
sql="insert into car (make, model, registration, price) values (%s,%s,%s,%s)"
#values = ("Ferrari","Daytona", "69G101",1000000)
#values = ("lamborghini","countach","75G200",2000000)
values = ("Porsche","959","81D400",2000000)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()