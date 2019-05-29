print "==========function test ===================="
def basicInfo(name,age):
    print 'name is:',name
    dictA = {}
    dictA['name'] = name
    dictA['age'] = age
    return dictA

dictB = basicInfo('lixue','28')
print 'dictB:',dictB
print "=========import module====================="
import sayHi
sayHi.lxSayHi()  
print "=========globals() and locals()============"
def testGL():
    localA = "localAstr"
    print 'glabals():',globals()
    print 'locals():',locals()
testGL()
#print "==========input============================="
#strA = raw_input("input your name:")
#print "Welcome %s !" %(strA)

#strB = input("input your lucky num: ")
#print "Nice number: %s" %(strB)
print "===========open and close file=============="
fo = open("foo.txt","w+r")
print 'fo.name:',fo.name
print 'check where file closed: fo.closed:',fo.closed
print 'check access mode fo.mode:',fo.mode
fo.write("lixue is writing here")
position = fo.tell()
print 'fo.tell(),get current position:',position
##redirect to start
currentPo = fo.seek(0,0)
print 'fo.seek(0,0) back to original position:',currentPo
fileStr = fo.read(256)
print'fo.read(256):',fileStr
fo.close()
print 'check where file closed: fo.closed:',fo.closed
print "=============== os ==========================="
import os
print 'os.mkdir("tempDir")'
os.mkdir("tempDir")
print "os.getcwd() get current directory:",os.getcwd()
originDir = os.getcwd()
os.chdir("/root/lixue/tempDir")
print "os.getcwd() get current directory:",os.getcwd()
os.chdir(originDir)
print "back to origin Dir:",os.getcwd()
os.rmdir("tempDir") 
print "================try -> except -> else=============="
try:
    fo = open("test.file","r")
    fo.write("this is a testing file")
except Exception,errX:
    print "occurs Exception:",errX
except IOError,e:
    print "Error: ",e
else:
    print "Everything is fine !"

#define my Error
def mye(level):
    if level < 1:
       raise Exception,"Invalid level"
try:
    mye(0)
except Exception,e:
    print "Error",e
else:
    print "Every thing is fine !"

print "================= exec =============================="
exec('print "I am using exec"')
