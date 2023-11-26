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
sql="select * from car where id = %s"
values = (1,)

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
  print(x)

db.close()
cursor.close()