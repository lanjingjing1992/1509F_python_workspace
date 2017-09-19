keymap={'a':1,'a':2,'c':3}
# print(keymap['a'])#根据键访问字典的值
# keymap['a']=4#修改字典的值
# print(keymap)
# del keymap['a']#删除指定位置的值
# print(keymap)
# # del keymap#删除字典
# keymap.clear()#只清空字典内的元素 保留字典对象
# print(keymap)
print(keymap)#如果两个键相同 ，前一个会被最后一个覆盖
#键是不可以改变的 所以可以用 元组，字符串，数值 但是不能用列表
# dict={('name',2):'张三',2:12,'height':100}
# print(dict)  #这是允许的
#
# dict={['name',2]:'张三',2:12,'height':100}
# print(dict) # 这样会报错  自己尝试