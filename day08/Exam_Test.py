# import time
# #定义一个列表
# list=[4,3,2,1]
# for i in list:
#     time.sleep(1)#每隔一秒输出一个元素
#     print(i)

list=[]
for i in range(3):
    num=int(input('请输入a,y,z'))
    list.append(num)
print(sorted(list))#排序后从小到大输出


