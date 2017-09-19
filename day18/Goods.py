class Goods:
    def __init__(self):
        self.food={'苹果':10,'苹果':2,'面包':3}
        self.life={'牙膏':5,'袜子':2}
        self.ball={'排球':12,'足球':100}
        self.all='商品种类 商品名称 单价  数量 小计\n'
        self.count=0
        self.kind={'food':self.food,'life':self.life,'ball':self.ball}