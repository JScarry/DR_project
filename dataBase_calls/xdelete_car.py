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
sql="delete from car where id = %s"
values = (4,)

cursor.execute(sql, values)

db.commit()
print("delete done")

db.close()
cursor.close()