import pymysql

q1 = input()
q2 = input()
query = input()

conn = pymysql.connect(host='localhost', port=3306, user='root', password='1234', db='pythondb', charset='utf8')

try:

    with conn.cursor() as curs:
        # sql = "select firstName from test where lastName = %s"
        sql = "select " + q1 + " from test where " + q2 + " = %s"
        print(sql)
        curs.execute(sql, query)
        # rs = curs.fetchall()
        rs = curs.fetchone()

    print(rs)

    '''
    def insert_row(cursor, data, table):

        placeholders = ', '.join(['%s'] * len(data))
        columns = ', '.join(data.keys())
        updates = []
        key_placeholders = ', '.join(['{0}=%s'.format(k) for k in data.keys()])
        sql = "INSERT INTO %s ( %s ) VALUES ( %s ) ON DUPLICATE KEY UPDATE %s" % (table, columns, placeholders, key_placeholders)
        cursor.execute(sql, data.values() * 2)

    '''

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
