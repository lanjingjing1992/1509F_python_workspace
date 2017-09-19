# list=[1,2,3,4,5]
# for i in range(len(list)-1,-1,-1):
#     print(list[i],end='  ')


# M Tu W Th F Sa Su
# while True:
#     s=input('请输入星期几')
#     if s[0]=='M':
#         print('星期一')
#     elif s[0]=='T':
#         if s[1]=='u':
#             print('星期二')
#         elif s[1]=='h':
#             print('星期四')
#         else:
#             print('都不是')
#     elif s[0]=='W':
#         print('星期三')
#     elif s[0]=='F':
#         print('星期五')
#     elif s[0]=='S':
#         if s[1]=='a':
#             print('星期六')
#         else:
#             print('星期日')
# 题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# list=[]
# for i in range(1,5,1):
#     for j in range(1,5,1):
#         for k in range(1,5,1):
#             if(i!=j and j!=k and i!=k):
#                 sum=i*100+j*10+k
#                 if sum not in list:
#                     list.append(sum)
#
# print(list)
#题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分
# ，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万
# 之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提
# 成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求
# 应发放奖金总数？
# bonus1=100000*0.1
# bonus2=bonus1+100000*0.75
# bonus4=bonus2+200000*0.5
# bonus6=bonus4+200000*0.3
# bonus10=bonus6+400000*0.15
# mon = int(input("请输入月利润:\n"))
# if mon<=100000:
#     bonus=mon*0.1
# else:
#     if mon<=200000:
#         bonus=bonus1+(mon-100000)*0.075
#     else:
#         if mon <= 400000:
#             bonus = bonus2 + (mon - 200000) * 0.05
#         else:
#             if mon <= 600000:
#                 bonus = bonus4 + (mon - 400000) * 0.03
#             else:
#                 if mon <= 1000000:
#                     bonus = bonus6 + (mon - 600000) * 0.015
#                 else:
#                     if mon > 1000000:
#                         bonus = bonus10 + (mon - 1000000) * 0.01
# print (bonus)
# # 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# for i in range(1000):
#     for j in range(1000):
#         if i*i+168==j*j:
#             num=j*j-268
#             if num>0:
#                 print(num)
#题目：输入某年某月某日，判断这一天是这一年的第几天？
# data=input('输入年月份,格式2016-05-12:')
# #字符串切割
# s=data.split('-')#以-为标志切割
# if(len(s)==3):
#     # 赋值
#     year = int(s[0])
#     mon = s[1]
#     day = s[2]
#     print (mon)
#     # python没有switch case 用字典方式
# else:
#     print ('输入有误')
# da={'1':0,'2':31,'3':59,'4':90,'5':120,'6':151,
#     '7':181,'8':212,'9':243,'01':0,'02':31,'03':59,
#     '04':90,'05':120,'06':151,'07':181,'08':212,'09':243,
#     '10':273,'11':304,'12':334}
# def f(x):
#     return da.get(x)
# sum=int(f(mon))+int(day)
# if(year%400==0 or (year%4==0 and year%100!=0)):
#     if(int(mon)>=3):
#         sum=sum+1
# print (sum)
# # 题目：输出9*9口诀。
# for i in range(1,10,1):
#     for j in range(1,i+1,1):
#         print('{}*{}={}'.format(i,j,i*j),end='   ')
#     print(end='\n')
# 打印出所有的"水仙花数"
for i in range(100,1000,1):
    a=i//100
    b=i%100//10
    c=i%10
    if a**3+b**3+c**3==i:
        print(i)