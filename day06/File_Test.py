import os
import shutil
# # file=open('file.txt','w+')#文件的名字  可写模式写入 如果没有指定路径 那么所有的文件就创建在当前路径下
# # file.write('helloworld')#写入内容
# # print(file.tell())#返回当前光标的位置
# # file.seek(1,0)#第二个参数代表从哪里开始 0代表是从开始位置 2代表的是结束为止 1代表的是当前位置 第一个参数代表隔几个
# # print(file.read(2))#读取内容  参数代表读取多少个字符
# # file.close()
# print(os.getcwd())#当前的路径
# os.chdir('D:\\')#改变当前路径
# print(os.getcwd())
# os.mkdir('test')#创建文件夹 注意 不能重复创建
# # os.rmdir('test')#移除文件夹 注意不能是非空文件夹
# shutil.rmtree('test')#用来移除非空文件夹
#
#
def file(path,data,fileName):

    os.chdir(path)#改变当前路径
    f = open(fileName,'a')  # 文件的名字
    f.writelines(data)
    # print(f.read())
    f.close()

