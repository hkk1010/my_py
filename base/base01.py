#!/usr/bin/python3
# coding:utf-8
import time
import sys


class Employee:
     empcount=0

     def __init__(self,name,salary):
         self.name=name
         self.salary=salary
         Employee.empcount+=1


     def displayname(self):

        print(self.name,self.salary,self.empcount)


em1=Employee('app01','12345')

em1.displayname()

print(Employee.empcount)