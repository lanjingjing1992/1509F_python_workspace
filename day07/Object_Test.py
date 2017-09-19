# class Test:#定义类名  注意符合标识符的命名规则
#     #构造方法
#     def __init__(self):
#         #用来写初始化的内容
#         self.age=10#使用self初始化年龄为10岁属性
#         self.height=100#初始化身高属性
#         self.name='Alice'#初始化一个姓名
#
#     #方法
#     def  sleep(self,height):
#         self.age+=1#对年龄属性加1
#         print(self.age)#打印出年龄
#         self.name+='Green'
#         print(self.name)
#         self.height=height
#         self.height+=1
#         print(self.height)
#
#      #对象名=类名（） 实例化对象的格式
# obj= Test()
# obj.sleep(10)#使用对象调用方法


# class Animal:
#     def __init__(self,name='world',health=100,love=100):
#         self.love=love
#         self.health=health
#         self.name=name
#     def sleep(self):
#         self.health-=1
#     def eat(self):
#         self.love+=1
#     def __del__(self):
#         print('垃圾回收')
#
#
# cat=Animal()
# cat.sleep()
# cat.eat()
#
# print(cat.love)
# print(cat.health)
# print(cat.name)
# print(cat.love)
# class Father:
#     def __init__(self):
#         self.name=''
#         print('父类的构造方法')
#     def eat(self):
#         print('父类的普通方法')
#
#
# class Son(Father):
#     def __init__(self):
#         Father.name='love'
#         Father.__init__(self)#注意：需要使用父类的类名来调用 参数必须是self
#
#         print('子类的构造方法')
#
#
#     def eat(self):
#         pass
#     def sleep(self):
#         self.eat()
#
# s=Son()#实例化子类的对象
# class Animal:
#     def __init__(self,name='alice',health=100):
#         print('父类构造方法')
#         self.name=name
#         self.health=health
#     def __eat(self):#私有类型 只有本类能够访问
#         print('父类的吃东西方法')
#     def _sleep(self):#受保护类型  只有本类以及子类能够访问
#         print('普通方法')
#
#
# class Dog(Animal):
#     def __init__(self,love=100):
#         Animal.__init__(self)
#         self.love=love
#     def eat(self):
#
#         Animal._sleep()
#         print('子类吃东西的方法')
#
#     # def sleep(self):
#     #
#     #     print('子类的睡觉方法')
#
# #
# #
# dog=Dog()
#
# dog.eat()
# dog.sleep()
# dog.name='lili'
# dog.love=1
# dog.health=1
# print(dog.name)
# print(dog.health)
# print(dog.love)
#重载  子类跟父类的方法名相同

class A:
    def __init__(self):
        pass
    def eat(self):
        print('父类的eat方法')

class B(A):
    def __init__(self,height=100):
        self.height=height
        pass
    def sleep(self):

        print('子类的睡觉方法')
    def eat(self):
        print('子类的eat方法')
    def __add__(self, other):
        return self.height+other.height


# b=B()
# b.sleep()
# b.eat()
b1=B()
b2=B(10)
print(b1+b2)