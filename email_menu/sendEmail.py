'''发送带附件的邮件'''
import smtplib
from  email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

msg=MIMEMultipart()
msg['From'] = '15901337131@163.com'
msg['To']=','.join(['18612254394@163.com'])
msg['Subject']='Report'
txt=MIMEText('作业敬请查看附件')
msg.attach(txt)
fileName='test.txt'

att1 = MIMEImage((lambda f: (f.read(), f.close()))(open(fileName, 'rb'))[0], _subtype ='')
att1.add_header('Content-Disposition', 'attachment', filename = fileName)
msg.attach(att1)
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com:25')
smtp.login('15901337131@163.com', '442131zkk')
smtp.sendmail(msg['From'], msg['To'], msg.as_string())
smtp.quit()
