#!/usr/local/bin/python
#-*- coding: utf-8 -*-
import re,sys,re
import string
import signal
 
def sigint_handler(signum, frame):
  global is_sigint_up
  is_sigint_up = True
  print 'catched interrupt signal!'
 
#
signal.signal(signal.SIGINT, sigint_handler)
 
#以下那句在windows python2.4不通过,但在freebsd下通过
signal.signal(signal.SIGHUP, sigint_handler)
 
signal.signal(signal.SIGTERM, sigint_handler)
is_sigint_up = False
 
# 循环
while True:
  try:
    # 你想做的事情
    print 'hello'
    if is_sigint_up:
     # 中断时需要处理的代码
      print "Exit"
      break
  except Exception, e:
    #  这里发生错误时需要写的代码
    break