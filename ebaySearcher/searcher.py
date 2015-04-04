import urllib2
import sys
import time
import random

ITEM_SUM = 10000
ITEM_IDX = 0
sellers = dict()

def pause(t=5):
  #time.sleep(random.uniform(5, 10))
  pass

def findSellers(url, pageItemNum, fetchSellerMethod, param):  
  pageNum = ITEM_SUM / pageItemNum
  for i in range(1, pageNum):
    pause(10)
    url = makeUrl(url, i, pageItemNum)
    #print 'processing %s' % (url,)
    items = fetchItems(url)
    for itm in items:
      seller = fetchSellerMethod(itm, param)
      if((seller is not None) and (not sellers.has_key(seller.name))):
        sellers[seller.name] = seller
        
def printSeller(seller):
  print 'find seller: %s score: %d' % (seller.name, seller.score)
def printSeller2(seller):
  print 'find seller: %s ' % (seller.name, )

def makeUrl(url, idx, pageItemNum):
  # replace page idx
  url = url.replace('_pgn='+str(idx-1), '_pgn='+str(idx))
  # replace skc
  url = url.replace('_skc='+str(pageItemNum*(idx-1)), '_skc='+str(pageItemNum*idx))
  return url

def fetchItems(url):
  pause()
  items = dict()
  # read url's content
  response = urllib2.urlopen(url)
  content = response.read()
  # find item
  key = '/itm/'
  pos = content.find(key, 0)
  while(pos != -1):
    # fetch item url
    beg = content.rfind('"', 0, pos)
    end = content.find('"', pos)
    itemUrl = content[beg+1:end]
    if(not(items.has_key(itemUrl))):
      items[itemUrl] = ''
      
    pos = content.find(key, pos+len(key))
    
  # save item
  return items
  
class Seller:
  pass
  

def fetchSellerByFeedback(url, param):
  limit = int(param)
  #print 'processing item %s' % (url,)
  # read url
  pause()
  response = urllib2.urlopen(url)
  content = response.read()
  # find score
  key = 'feedback score: '
  beg = content.find(key)
  if(beg != -1):
    end = content.find('"', beg)
    if(end != -1):
      score = int(content[(beg+len(key)):end])
      seller = Seller()
      seller.score = score
      global ITEM_IDX
      ITEM_IDX += 1
      print 'item %s score: %d' % (itemIndex(ITEM_IDX), score)
      if(score < limit):
        # if score is ok, fetch seller
        key = '/usr/'  
        beg = content.find(key)
        if(beg!=-1):
          end = content.find('?', beg)
          seller.name = content[(beg+len(key)):end]
          return seller

def fetchSellerByKeywords(url, param):
  #print 'processing item %s' % (url,)
  # read url
  pause()
  response = urllib2.urlopen(url)
  content = response.read()
  global ITEM_IDX
  ITEM_IDX += 1
  print 'item %s' % (itemIndex(ITEM_IDX))
  # find keywords
  keywords = param
  beg = content.find(keywords)
  if(beg != -1):
    # if find keywords, fetch seller
    key = '/usr/'  
    beg = content.find(key)
    if(beg!=-1):
      end = content.find('?', beg)
      seller = Seller()
      seller.name = content[(beg+len(key)):end]
      return seller
          
def itemIndex(idx):
  s = str(idx)
  for i in (range(len(str(ITEM_SUM))-len(str(idx)))):
    s = '0'+ s
  return s

import re,sys,re
import string
import signal
 
def sigint_handler(signum, frame):
  # print sellers
  print ''
  for seller in sellers.values():
    printSeller2(seller) 
  sys.exit(0)
 
#
signal.signal(signal.SIGINT, sigint_handler)
 
#signal.signal(signal.SIGHUP, sigint_handler)
 
signal.signal(signal.SIGTERM, sigint_handler)

def isNum(o):
  try:
    int(o)
    return True
  except:
    return False

if(__name__=='__main__'):
  # argv[1] url
  # argv[2] pageItemCount
  # argv[3] feedbackLimit or keywords
  # if argv[3] is number, feedbackLimit
  # else keywords
  if(isNum(sys.argv[3])):
    findSellers(sys.argv[1], int(sys.argv[2]), fetchSellerByFeedback, sys.argv[3])
  else:
    findSellers(sys.argv[1], int(sys.argv[2]), fetchSellerByKeywords, sys.argv[3])
  