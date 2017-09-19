import math
# #Python程序从屏幕输入两个数字，并且输出这两个数字的和
def f3():
    num1=int(input('请输入第一个数字：'))#从屏幕输入数字，但这是字符串格式，所以还要转换为int格式
    num2=int(input('请输入第二个数字:'))
    print('两个数字的和是%s'%(num1+num2))
#
#
#
#Python程序从屏幕循环输入数字，存到列表
# list=[]#先定义一个空的列表
# for i in range(3):#for循环输入
#     num=int(input('请输入数字：'))#获取输入的数字
#     list.append(num)#添加到列表
#
# print(list)#打印列表
## #Python程序从屏幕循环输入数字，存到列表
# list=[]#先定义一个空的列表
# for i in range(3):#for循环输入
#     num=int(input('请输入数字：'))#获取输入的数字
#     list.append(num)#添加到列表
#
# print(list)#打印列表
#
def f1():
   #先定义出三边
   a=2
   b=3
   c=4
   #周长的一半
   p=0.5*(a+b+c)
   #海伦公式 s=sqrt(p*(p-a)*(p-b)*(p-c))
   s=math.sqrt(p*(p-a)*(p-b)*(p-c))
   print('面积为：%s'%s)
   # 斐波拉契函数
def f2(j):

    list=[1,1]
    for i in range(j):
        if i==0:#如果是第一个数字的话也就是下标为0  则直接打印这个数
            print(list[0])
        elif i==1:#如果是第二个数字的话也就是下标为1  则直接打印这个数
            print(list[1])
        else:
            num=list[i-1]+list[i-2]#其他的数字则打印之前两个数字的和  并且添加到列表中
            list.append(num)


    print(list)#打印列表