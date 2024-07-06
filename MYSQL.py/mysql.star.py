import mysql.connector
#連線到資料庫
con=mysql.connector.connect(
    user="root",
    password="7121gary",
    host="localhost",
    database="themain"
)
print("資料連線成功")
  

cursor=con.cursor()#建立cursor物件，用來對sql下指令
cursor.execute("select * from product")
data=cursor.fetchall()
for row in data:
    print(row[0],row[1])
# cursor.execute("select * from product where id=3")
# data=cursor.fetchone()#取得單筆資料
# print(data)
# print(data[0],data[1])
# productname="普洱拿鐵"
# productid=7
# cursor.execute("update product set name=%s where id=%s",(productname, productid))#塞入sql指令#也可以用來做更新動作
# con.commit()#確定執行

con.close()#關閉資料庫連線