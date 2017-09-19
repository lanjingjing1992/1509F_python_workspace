import time#引入时间的包
import random#引入随机数的包
s=time.strftime('%Y%m%d',time.localtime())#获取本地时间并且时间格式化
t='测试报告'
r=random.randint(1,100)#获取随机数
print(t+s+str(r))#打印 并且将int类型转换成string类型

for i in range(1,8,2):#从1到8 每次加2  但是不包括8 包括1
    t=(7-i)//2#打印空格的个数  //表示只取整数部分
    print(' '*t+'*'*i+' '*t)#空格 加 星号  加  空格
for i in range(7,0,-2):#从7到0 吗每次减2  不包括0 包括7
    t=(7-i)//2#打印空格的个数  //表示只取整数部分
    print(' '*t+'*'*i+' '*t)#空格 加 星号  加  空格