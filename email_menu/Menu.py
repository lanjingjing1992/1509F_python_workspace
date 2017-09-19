#encoding=utf-8
import pymysql
from datetime import  datetime
import os
import email_menu.sendEmail
now=datetime.now()
i=datetime.strftime(now, '%Y-%m-%d')
print(type(i))


db=pymysql.connect(host='localhost',user='root',passwd='123456',db=' scheduled',charset='utf8')
cursor=db.cursor()


# sql="SELECT sch.`date`,employee.`name`,menu.`name` FROM employee JOIN " \
# " sch ON employee.`id`=sch.`employeeid` JOIN menu ON menu." \
# "`id`=sch.`foodid` WHERE sch.`date`= "+i
# sql.replace('aaa',i)
# print(sql)
sql="SELECT sch.`date`,employee.`name`,menu.`name`" \
    " FROM employee JOIN  sch ON employee.`id`=sch.`employeeid`" \
    " JOIN menu ON menu.`id`=sch.`foodid` WHERE sch.`date`='%s'"%i

print('今天的订餐sql：'+sql)
cursor.execute(sql)
data2 = cursor.fetchall()
# print(data2)
os.chdir('d:\\')#切换路径到D盘
print(os.getcwd())#获取当前的路径

file=open('foo.xls','w')#创建一个名为foo的excel文档


for i in range(len(data2)):
  print(data2[i])
  for j in range(3):
     file.write(str(data2[i][j]))#将内容按照一条一条的写入到excle表中

mailto_list = ["18612254394@163.com"]  #目标邮箱
print(type(file.name))
print(os.getcwd())
hello.sendEmail.send_mail(mailto_list,"点餐系统","如下是我们今天的菜单",file.name)
print("操作成功")






