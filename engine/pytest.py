import numpy as np
import itertools
counts = 0
for i in itertools.permutations("1234",3):
    counts += 1


#print(next(itertools.permutations("1234",3)))
import pymysql

conn= pymysql.connect(
host='localhost',
port = 3306,
user='root',
passwd='',
db ='test',
)

cur = conn.cursor()
#创建数据表
#cur.execute("create table student(id int ,name varchar(20),\
#    class varchar(30),age varchar(10))")

#cur.execute("insert into student values('2','Tom',\
#    '3 year 2 class','9')")

#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class'\
#        where name = 'Tom'")
#删除查询条件的数据
#cur.execute("delete from student where age='9'")

#一次插入多条记录
sqli="insert into student values(%s,%s,%s,%s)"
cur.executemany(sqli,[
('3','Tom','1 year 1 class','6'),
('3','Jack','2 year 1 class','7'),
('3','YinLiqing','2 year 2 class','7'),
])
cur.close()
conn.commit()
conn.close()