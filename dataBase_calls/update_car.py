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
sql="update car set Make= %s, Model=%s, Registration=%s, Price=%s where id = %s"
values = ("Ferrari","F40","91D40",3000000, 1)

cursor.execute(sql, values)

db.commit()
print("update done")

cursor.close()
db.close()
