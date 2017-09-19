class Cargo:
    #初始化货物种类 价格
    def __init__(self):
        self.count=0
        self.all={}
        self.ball = {'羽毛球':1, '乒乓球':2, '足球':3}
        self.clothe = {'帽子':4, '上衣':5, '鞋子':6}
        self.food = {'方便面':7, '矿泉水':8, '面粉':9}
        self.fruit = {'葡萄':10, '西瓜':11, '榴莲':12}
        self.kind={'ball':self.ball,'clothe':self.clothe,'food':self.food,'fruit':self.fruit}
