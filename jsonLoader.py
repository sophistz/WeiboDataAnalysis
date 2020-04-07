import MySQLdb

db = MySQLdb.connect("localhost", "root", "taijiren007", "weibo", charset='gbk')

cursor = db.cursor()

sql = """SELECT * from fg_weiboinfo"""

cursor.execute(sql)

results = cursor.fetchall()

i = 0
for row in results:
    print(row[6], row[7])
    pass
