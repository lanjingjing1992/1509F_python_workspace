import pymysql#引入框架

db=pymysql.connect(host='localhost',user='root',passwd='123456',db='lanjingjing')#链接数据库
#游标 用来操作数据库
cursor=db.cursor()
# cursor.execute('create database lanjingjing')#执行操作
# cursor.execute('show databases')
# cursor.execute('create table test(id int,name varchar(20))')
# cursor.execute('show tables')
cursor.execute('insert into test(id,name) values (1,\'a\')')
cursor.execute('insert into test(id,name) values (2,\'b\')')
cursor.execute('insert into test(id,name) values (3,\'c\')')
db.commit()#提交数据
cursor.execute('select * from test')
data=cursor.fetchall()#查询出所有的数据
print(data)
