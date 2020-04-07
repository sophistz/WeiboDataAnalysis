import MySQLdb

db = MySQLdb.connect("localhost", "root", "taijiren007", "weibo", charset='gbk')

cursor = db.cursor()

sql = """SELECT * from fg_weiboinfo"""

cursor.execute(sql)

results = cursor.fetchall()

i = 0
j = 0
dictionary = {}
for row in results:
    if row[6] != "":
        i += 1
        if row[6] not in dictionary.keys():
            j += 1
            dictionary.update({row[6]: []})
            pass
        if row[0] not in dictionary.keys():
            j += 1
            dictionary.update({row[0]: []})
            pass
        if row[0] != row[6]:
            dictionary[row[6]].append(row[0])
        pass
    pass
print(len(dictionary.keys()), i, j)
# print(dictionary)

with open('test.json', 'r+') as jsonFile:
    jsonFile.write(str(dictionary).replace('\'','\"'))
    pass


