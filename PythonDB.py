import pymysql

query = input()

conn = pymysql.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')

try:

    with conn.cursor() as curs:
        sql = "select firstName from test where lastName = %s"
        print(sql)
        curs.execute(sql, query)
        rs = curs.fetchall()
    
    print(rs)

    '''
    with conn.cursor() as curs:
        sql = "insert into test(lastName, firstName) values (%s, %s)"
        curs.execute(sql, ("yoo", "jinseok"))

    conn.commit()
    '''
    '''
    with open('C:/Users/USER/Desktop/Python-Basic/db.txt', 'a') as f:
        for data in rows:
            d = str(list(data)) + '\n'
            f.write(d)
    '''

finally:
    conn.close()

'''
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str = ''.join(tup)
print(str)
'''
