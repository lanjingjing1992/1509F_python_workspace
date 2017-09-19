import pymysql

db=pymysql.connect(host='localhost',db='lanjingjing',passwd='123456',user='root',charset='utf8')
cursor=db.cursor()
k=input('请输入种类')
n=input('请输入名称')
cursor.execute('select * from kind')
data=cursor.fetchall()
k_list=[]
for i in range(len(data)):
    k_list.append(data[i][0])
print(k_list)
if k in k_list:
    cursor.execute('select * from %s'%k)
    data = cursor.fetchall()
    n_list = []
    for i in range(len(data)):
        n_list.append(data[i][0])
    print(n_list)
    if n in n_list:
        cursor.execute('select price from %s'%k+' where name=%s' ,(n) )
        data=cursor.fetchone()
        price=data[0]
        num=int(input('请输入数目'))
        print(price*num)


