#递归  自己调用自己

#
# def function(i):
#     if i==1:
#         return 1
#     elif i==2:
#         return 1
#     else:
#         return function(i-1)+function(i-2)
#
# def func(i):
#     if i==1:
#         return 1
#     else:
#         return i*func(i-1)
#
# print(func(5))
# print(function(10))
# s='HelloWorld'
# for i in s:
#     if i.islower():
#        print(i,end=';')
# def f():
#     s = input('请输入一个字母：')
#     if s in 'helloworld':
#         print("这个字母在其中")
#     else:
#         print("这个字母不在其中")
#         f()
#
#
# f()
# a = 2
# b = 3
# c = a**b
# print ("c 的值为：%s"%c)

s='helloworld'
# print(s[2:4])#包左不包右  从下标2到3将打印出来
# print(s.count('l'))
# print(s.count('o'))
# l=s.capitalize()
# print(l)
# print(s.endswith('d'))
#string.find(str, beg=0, end=len(string))

# string.isalnum()
#
# string.isalpha()
#
# string.isdigit()
#
# string.islower()
#
# string.lower()
#
# string.upper()
#
# string.lstrip()
# max(str)
# min(str)
# string.replace(str1, str2,  num=string.count(str1))
#
# string.rstrip()


# print('''hello
#
# i
#     am here''')
# print('hello i '
#       ''
#       ''
#       'am here')
# k=s.capitalize()
# print(k)
# for i in range(len(s)):
#     print(s[i],end='')
#
# for i in s:
#     print(i,end='')
#
# print(s[:len(s)])
# print(s[0:2])
# print(s*3)

list=['hello',1,2,0.02]
print(list[1:])