print "===========for date================="
import time
print time.time()
print 'time.localtime:',time.localtime(time.time())
localtimeA = time.asctime(time.localtime(time.time()))
print 'localtimeA:',localtimeA
formatTimeB = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print 'formatTimeB:',formatTimeB
## transfer format string to timestamp
timeB = time.mktime(time.strptime(formatTimeB,"%Y-%m-%d %H:%M:%S"))
timeA = time.mktime(time.strptime(localtimeA,"%a %b %d %H:%M:%S %Y"))
print 'timeA:',timeA
print 'timeB:',timeB
print 'time.timezone:',time.timezone
print 'time.tzname:',time.tzname
## datetime
import datetime
dateTime = datetime.datetime.now()
print "current Y is %s,M is %s,h is %s" %(dateTime.year,dateTime.month,dateTime.hour)

print "===========for test================="
#for i in range(1,5):
 #   if i == 3:
  #      pass
   #     print "here is pass module"
    #print "here is num " + str(i)
print "===========dic test================="
dict = {'name':'lixue','age':28}
print " here is the dice",dict
print dict.keys()
print dict.values()
print dict['name']
print "===========str format test ========"
print "my name is %s, age is %d" %(dict['name'],dict['age'])
print "===========str(),tuple(),dict() transition===="
list1 = list(dict)
print "here is list" + str(list1)
tuple=('red','green','blue')
list2 = list(tuple)
print list2
list2[1]='updated'
print list2
print "==========tuple test =============="
print tuple
#tuple[2]='lixue'
print tuple
print tuple[2]
print "==========list test ==============="
listA = ['lixu','xiaoxue',232,34]
listB = ['listB']
print listA
print listB
print listA.append('strB')
print listA + listB
print listA[1]
print listA[1:2]
print listA[1:3]
print listA[0:1] + listA[3:4]
s='2019.05.002'
print s[0:7]
print "=========triple double quotation marks======================="
paragraph = """
here is the introduction.
I am lixue
"""
print paragraph

