# import os
# #首先在D盘创建文件test1
# os.chdir('d:\\')#切换到D盘下
# file1=open('test1.txt','w+')
# file1.write('hello')
# file1.seek(0,0)
# data1=file1.read()
# print(data1)
# file1.close()
# os.chdir('D:\web_workspace')
# file2=open('test2.txt','w+')
# file2.write('world')
# file2.seek(0,0)
# data2=file2.read()
# print(data2)
# file2.close()
# data=data1+data2
# file3=open('C.txt','w+')
# file3.write(data)
# file3.seek(0,0)
# print(file3.read())
# file3.close()
# print('大功告成！！！')
#
class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)


    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)



#"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
#"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

