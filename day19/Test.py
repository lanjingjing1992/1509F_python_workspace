from day19.Menu import *
class Test:
    def __init__(self):
        self.menu=Menu()
        self.all=''
        self.count=0
    def login(self):
        identity=input('如果您是管理员则输入1，如果是顾客请输入其他')
        if identity=='1':
            name=input('请输入管理员姓名')
            passwd=input('请输入管理员密码')
            if name=='admin' and passwd=='123':
                #添加编号 菜名  单价
               num=len(self.menu.menu)
               print('当前的编码为'+str(num))
               name=input('请输入新的菜品名称')
               price=int(input('请输入新的菜品单价'))

               self.menu.menu.update({num+1:[name,price]})
               print(self.menu.menu)
               print('更新成功')
               self.order()
            else:
                print('管理员身份已锁定，即将退出')
                return

        else:
            self.order()
            y_n=input('是否继续点餐（结束输入n,继续可按任意键）')
            if y_n=='n':
                #结账
                print('您的点餐信息如下\n'
                      '*****************************\n'
                      +"编号"+"   "+"菜品名称"+"   "+"价钱"+"   "+"数量"+"   "+"小计")
                #写入文件
                file=open('test.txt','w+')
                file.write(self.all)
                file.seek(0,0)
                print(file.read())
                file.close()
                print('-------------------------------\n合计                 '+str(self.count)+'元\n'+'***************************')

            else:
                self.order()

    def order(self):
        print('菜品展示\n------------------------------\n'
              '编号       菜品名称      价格\n')
        for i in range(len(self.menu.menu)):
            print('%s      '%(i+1),end='')
            print(self.menu.menu[i+1][0] + '        ',end='')
            print(str(self.menu.menu[i+1][1]))
        print('\n------------- ---------------\n'
                  '\n'
                  )
        id = input('请根据菜单输入您所需菜品的编号:')
        num = input('请输入您所需菜品的数量')
        price=self.menu.menu[int(id)][1]
        menu_name=self.menu.menu[int(id)][0]
        sum=price*int(num)
        self.count+=sum
        self.all+=id+'   '+'   '+menu_name+'    '+str(price) +'元   '+num+'    '+str(sum)+'元'


t=Test()
t.login()
