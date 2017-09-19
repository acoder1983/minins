#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import time
import urllib2
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="acoder1984"    #用户名
mail_pass="Giszorro1983"   #口令 
 
 
sender = 'acoder1984@163.com'
receivers = ['acoder1984@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

def fetchIp():
    response=urllib2.urlopen('http://www.net.cn/static/customercare/yourip.asp')
    page=response.read()
    p=re.compile('\d+\.\d+\.\d+\.\d+')
    m=p.search(page)
    return m.group()

my_ip = None

while True:
    try:
        ip=fetchIp()
        if ip != my_ip:
            my_ip=ip
            print my_ip
            message = MIMEText(my_ip, 'plain', 'utf-8')
            subject = my_ip
            message['Subject'] = Header(subject, 'utf-8')
             
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
            smtpObj.login(mail_user,mail_pass) 
            smtpObj.sendmail(sender, receivers, message.as_string())
            smtpObj.close()
    except Exception, e:
        print e

    time.sleep(30)

