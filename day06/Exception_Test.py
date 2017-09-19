import os
import shutil
# list=[1,2,3]
# print(list[3])#IndexError 下标越界异常
# print('hello'+2)#typeError 类型错误
# file=open('s.txt','r+')#FileNotFoundError 文件找不到异常
# # os.rmdir('test')#os异常
# try:
#     os.rmdir('test')
#     print('没有发生异常')
# except OSError:
#     print('发生了异常')
#     import shutil
#     shutil.rmtree('test')
#     #如果没有发生异常则只执行try里面的代码 如果发生了异常 就会跳转到except中执行代码
# finally:#不管有没有发生异常都需要执行的代码

try:

    file=open('test.txt','r')
except (FileNotFoundError,IOError):
    print('创建文件失败,将使用另外一种方式创建文件')
    file=open('test.txt','w')

finally:
    print(file.name)


