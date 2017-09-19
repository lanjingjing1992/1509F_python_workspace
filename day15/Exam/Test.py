from day15.Exam.Person import *
from day15.Exam.Cargo import *
import os
class Test:
    def __init__(self):
        self.p = Person()
        self.c= Cargo()
    def Login(self):
        #登陆验证
        self.name=input('请输入姓名')
        self.password=input('请输入密码')
        #创建person对象

        print('在查找姓名之前打印所有的名字')
        print(self.p.map.keys())
        if self.name in self.p.map.keys():#用户名存在的
            if self.password==self.p.map[self.name]:#密码一致
                print('登陆成功！！！')
                self.Calc()
                return
            else:
                print('密码输入错误')
                self.Login()
        else:
            print('注册')#像字典中添加键值对
            self.p.map.update({self.name:self.password})
            self.Login()





    def Calc(self):#计算商品总价 并且打印  单价*数量
        self.kind=input('请输入物品的种类：')
        self.cargoName=input('请输入物品名字：')
        self.num=int(input('请输入数量：'))
        if self.kind in self.c.kind.keys():
            if self.cargoName in self.c.kind[self.kind].keys():
                price=self.c.kind[self.kind][self.cargoName]#单价
                sum=price*self.num
                self.c.all.update({self.kind+'类'+self.cargoName+'物品'+str(self.num)+'个':sum})
                self.c.count+=sum
                y_n=input('是否继续输入y/n')
                if y_n=='y':
                    self.Calc()
                else:
                    #停止输入 在d盘下创建文件test.txt
                    shopping_list=self.c.all.keys()
                    self.writeAndRead(str(self.c.all))
                    print('总价格为：%s'%self.c.count)

            else:
                y_n=input('物品不存在 是否更新 y/n')
                if y_n=='y':
                    self.update(self.kind,self.cargoName)
                else:
                    return
                self.Calc()
        else:
            y_n=input('种类不存在，更新后请重新输入,是否更新')
            if y_n=='y':
                self.update(self.kind,self.cargoName)
            else:
                return
            self.Calc()

    def update(self,k,n):#更新库存内容
        price = int(input('请输入单价'))
        if k in self.c.kind.keys():#种类是存在的 只需要更新物品名称
            self.c.kind[k].update({n:price})
        else:#种类跟物品名称都不存在  则一起添加
            self.c.kind.update({k:{}})
            self.c.kind[k].update({n:price})


    def writeAndRead(self,n):#用来读写文件
        os.chdir('d:\\')
        self.file=open('test.txt','w+')
        self.file.write(n)
        self.file.seek(0,0)
        data=self.file.read()
        print(data)



t=Test()
t.Login()