from day18.Goods import *
from day18.Person import *
import os
class Buy:
    def __init__(self):
        self.p=Person()
        self.g=Goods()
    def login(self):
        n=input('请输入姓名')
        p=input('请输入密码')
        if n in self.p.map.keys():
            if p==self.p.map[n]:
                print('登陆成功，即将进入结算')
                self.calc()
            else:
                print('密码错误，已锁定')
        else:
            y_n=input('用户名不存在，是否注册y/n')
            if y_n=='y':
                self.p.map.update({n:p})
                print('注册完成，即将重新登陆系统')
                self.login()
            else:
                print('退出系统')
                return
    def calc(self):
        k=input('请输入种类：')
        n=input('请输入商品名称')
        num=int(input('请输入数量'))
        if k in self.g.kind.keys():
            price=self.g.kind[k][n]
            sum=num*price
            self.g.all+=k+' '+n+' '+str(price)+'*'+str(num)+'  '+str(sum)+'\n'
            self.g.count+=sum
            y_n=input('是否继续输入y/n')
            if y_n=='y':
                self.calc()
            else:
                self.g.all+='总计：'+str(self.g.count)
                self.w_r_file(self.g.all)

        else:
            y_n=input('商品不存在，是否添加到库存 y')
            if y_n=='y':
                if self.update(k,n):
                    print('更新成功，重新输入并且结算：')
                    self.calc()
                else:
                    return




    def update(self,k,n):
        print('接下来将以管理员身份登陆')
        name=input('请输入姓名')
        passwd=input('请输入密码')
        if name=='admin'  and passwd=='123':
            price=int(input('请输入单价'))
            self.g.kind.update({k:{n:price}})
            return True
        else:
            print('管理员身份已锁定，退出系统')
            return False

    def w_r_file(self,n):
        # os.chdir('d:\\')
        file=open('test.txt','w+')
        file.write(n)
        file.seek(0,0)
        print(file.read())
        file.close()



buy=Buy()
buy.login()
