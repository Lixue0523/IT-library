#!/usr/bin/python
print ("============basic Class ==============")
class Employee:
    empCount = 0
    def __init__(self, name, salary):
       self.name = name
       self.salary = salary
       Employee.empCount +=1
    def employInfo(self):
       print "name:%s,salary:%s" % (self.name,self.salary)
    def displayCount(self):
       print "Employee numbers: %d" % Employee.empCount

emp = Employee("lixue","4342")
emp.employInfo()
emp.displayCount()
print "=============class inheritance============"
class Manager(Employee):
    teamMember = 0
    def __init__(self,name,salary,level):
        Employee.__init__(self,name,salary)
        self.level = level
        print "Manager init"
    def setLevel(self,level):
        self.level = level
    def managerTask(self):
        if self.level > 5:
           print "High level: guiding  the team"
        else :
           print "Medium level: leading the team"
managerA = Manager("hh","34",5)
managerA.employInfo()
managerA.managerTask()
managerA.displayCount()
print "================= json ========================="
import json
data = {'name':'lixue','age':27}
jsonData= json.dumps(data)
print "data:",data
print "jsonData:",jsonData
#print "jsonData.name:",jsonData['name']
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
jsonDataA = json.loads(json_string)
print "json string data: ", jsonDataA
fo = open("json.txt","w")
fo.write(json_string)
fo.close()
print "================== socket ========================="
import socket
s = socket.socket()
hostname = socket.gethostname()
print "host is :", hostname
port = 12345
s.bind((hostname,port)) # double ()
s.listen(5)
while True:
    c,addr = s.accept()
    print "client address :",addr
    c.send('Welcome from server!')
    data = c.recv(1024)
    print('recive:',data.decode())
    c.close()


