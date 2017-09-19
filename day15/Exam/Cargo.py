class Cargo:
    def __init__(self):
                   #初始化库存中已经有的商品种类  每个种类中的商品名称  商品价格
          self.food={'面包':5,'牛奶':8,'水果':10,'辣条':1,'大辣皮':2}
          self.sport={'乒乓球':1,'篮球':30,'足球':50,'羽毛球':6}
          self.life={'毛巾':15,'牙刷':10,'洗面奶':75,'面膜':99}
          self.kind={'food':self.food,'sport':self.sport,'life':self.life}
          self.all={}
          self.count=0
