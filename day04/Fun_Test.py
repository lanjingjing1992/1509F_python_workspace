# def f1(a,*args):
#     print(a)
#     print(args)
#     # for i in args:
#     #     print(i)
#
# f1(1,2,3,4,5,'hello','a')#不定长
#
# #不可变  数字  字符串  元组
# #可变 列表 字典
# b=[1,2,3]
# a=1
# def f2(a):
#     print(a)
#
# f2(b)
#
#
# f3=lambda a,b,c:a+b+c
# print(f3(2,3,4))#匿名函数
#
# def f4():
#     return 1
#
# print(f4())
# a=1
# def f():#方法外面的是全局变量  方法里面的是局部变量
#     # a=6
#     global a
#     a=a+1
#     print(a)
# f()
#
# def f1():
#     a=1
#     def f2():
#         nonlocal a#用来标识  不仅改变方法内部的值  还改变其外部嵌套的变量值
#         a=2
#         print(a)
#     f2()
#     print(a)
#
#
# f1()
a=1
b=a
def f1(w):
    w=w+1
    print(w)
f1(a)
print(b)


a=[1,2,3]
b=a
def f2(w):
    w[0]=100
    print(w)
f2(a)
print(b)
