import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')

try:
    curs = conn.cursor()
    sql = "select * from test"
    curs.execute(sql)
    rows = curs.fetchall()

    with open('C:/Users/USER/Desktop/Python-Basic/db.txt', 'a') as f:
        for data in rows:
            d = str(list(data)) + '\n'
            f.write(d)

    print(rows)

finally:
    conn.close()

'''
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str = ''.join(tup)
print(str)
'''