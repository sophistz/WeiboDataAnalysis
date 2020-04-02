
import MySQLdb

db = MySQLdb.connect("localhost", "root", "taijiren007", "weibo", charset='gbk')

cursor = db.cursor()

sql = """SELECT * from rework"""

cursor.execute(sql)

results = cursor.fetchall()

i=0;
for row in results:
    if (row[2]=="王俊凯人工智能发电站"):
        print(row[4])
        i+=1
        pass
    pass
print(i)