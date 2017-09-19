import smtplib#用来发邮件的插件
from email.mime.multipart import MIMEMultipart #用来构建发件人 收件人  主题
from email.mime.text import MIMEText #用来构建正文部分

msg=MIMEMultipart()#用来存储发件人 收件人  主题
msg['from']='15901337131@163.com'#发件人地址
msg['to']=','.join(['18612254394@163.com'])#收件人地址
msg['subject']='作业'

text=MIMEText('这是今天的作业，已经认真完成，请查收')#正文部分
msg.attach(text)#添加到msg

smtp=smtplib.SMTP()#创建发邮件对象
smtp.connect('smtp.163.com:25')#链接服务器
smtp.login('15901337131@163.com','442131zkk')#登陆smtp的密码

smtp.sendmail(msg['from'],msg['to'],msg.as_string())
smtp.quit()






