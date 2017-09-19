#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="acoder1984"    #用户名
mail_pass="Giszorro1983"   #口令 
 
 
sender = 'acoder1984@163.com'
receivers = ['acoder1984@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('hello mail', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] =  Header("测试", 'utf-8')
 
subject = 'hello'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "send ok"
except smtplib.SMTPException, e:
    print e