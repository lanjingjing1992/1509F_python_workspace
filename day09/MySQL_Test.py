import pymysql#引入框架
from day06 import File_Test
import os

db=pymysql.connect(host='localhost',user='root',passwd='123456',db='lanjing',charset='utf8')#链接数据库
#游标 用来操作数据库
cursor=db.cursor()
# cursor.execute('create table pet(name varchar(50),age int,sex varchar(20))')
# cursor.execute('insert into pet(name,age,sex) values (\'lan\',10,\'men\')')
# cursor.execute(' insert into pet(name,age,sex) values (\'Lily\',12,\'women\')')
# cursor.execute(' alter table pet add weight int')
# cursor.execute(' update  pet set weight=100 where name=\'lan\'')
# cursor.execute('update  pet set weight=120 where name=\'Lily\'')
# db.commit()#提交数据
# cursor.execute('select * from pet')
# data=cursor.fetchall()#查询出所有的数据
# db.close()
# # print(data)
# for i in range(len(data)):
#     print(data[i])
#     for j in range(len(data[i])):
#         if i==0 and j==0:
#             File_Test.file('d:\\',str(data[i][j]),'mysql.txt','w+')
#         else:
#             File_Test.file('d:\\', str(data[i][j]), 'mysql.txt', 'a')

# File_Test.file('d:\\',str(data),'mysql.txt')
# os.chdir('d:\\')','r+')
# print(file.read())
# cursor.execute('CREATE DATABASE lanjing')
#
# cursor.execute('rename table lanjingjing.pet to lanjing.pet')
# db.commit()
# cursor.execute('use lanjing')
#
# # file=open('mysql.txt
# cursor.execute('create database wengning')
# cursor.execute('create table wengni(name varchar(20),age int,sex varchar(10))')
# cursor.execute('show tables')
# cursor.execute('alter table wengning modify sex varchar(100)')
# cursor.execute('insert into wengning(name,age,sex) values (\'lan\',10,\'men\')')
# cursor.execute('insert into wengning(name,age,sex) values (\'lily\',20,\'women\')')
# db.commit()
# cursor.execute('select * from wengning')
# cursor.execute('desc wengning')
# date=cursor.fetchall()
# print(date)
# # db.commit()
# cursor.execute('alter database lanjing character set utf8 ')
# cursor.execute('insert into pet1(name) values \'兰\'')
# db.commit()
# data=cursor.execute('select * from pet1')
# print(data)


