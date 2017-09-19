from day14.Cargo import *

from day14.Person import *


class Test:
    def login(self,p):
            #登陆
            self.name=input('请输入姓名')
            self.password=input('请输入密码')
            if self.name in p.map:
                if self.password==p.map[self.name]:
                    print('登陆成功')
                    cargo=Cargo()
                    self.Clac(cargo)
                    return
                else:
                    self.login(p)
            else:
                print('开始注册')
                p.map.update({self.name:self.password})
                self.login(p)

    def Clac(self,c):
        self.kind=input('请输入种类：')
        self.cargo=input('请输入物品名称：')
        self.num=int(input('请输入数量：'))
        if self.kind in c.kind.keys():
            if self.cargo in c.kind.get(self.kind):
                c.count+=c.kind.get(self.kind).get(self.cargo)*self.num
                c.all.update({self.kind+'类：' + self.cargo + str(self.num)+'个': str(c.count)+'元'})
                n=input('是否继续输入：y/n')
                if(n=='y'):
                    self.Clac(c)
                else:
                    print(c.all)
                    print('所以总价格为%s'%c.count)
            else:
                print(self.kind+'种类中没有此物品')
        else:
            print('无此类物品')
    def update(self):
        #用来更新添加Cargo中的种类
        pass









p=Person()
t=Test()
t.login(p)






