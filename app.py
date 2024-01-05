### Modules

import sqlite3
conn = sqlite3.connect('info')

cur = conn.cursor()

query_data = '''create table student(
                studentId int,
                firstname varchar (255),
                lastname varchar (255),
                address varchar (255),
                city varchar (255));'''

cur.execute(query_data)

conn.commit()
conn.close()


conn = sqlite3.connect('info')
cur = conn.cursor()
q1 = '''insert into student1(studentId,firstname,lastname,address,city)
         values('1','amol','naik','thergaon','pune');'''

cur.execute(q1)

conn.commit()
conn.close()


