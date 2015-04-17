#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Script Python Example
import time
import sys
import json
import makehtml
import MySQLdb
 
print "Initializing Python Script"

'''
Forms HTML
Text_Input('title')
Text_Area('desc')
Select('Hi','No')
Radio_Button('Radio1', 'Radio2')
Check_Box('Yes', 'No')
Static_Title(t)

'''

data  = sys.argv[1]
output = json.loads(data)
val1 = output['model'].values()
k=0
array = []
#Collected all the json values last three variables containing name and field type
for values in val1:
    var2 = val1[k].values()
    array.append( var2[3:])
    k+=1

html = ''
table = ''

#Get the key of dictioary for sorting out
def getKey(item):
    return item[1]

#Getting HTML for the fields
def Get_Data(t):
    length = len(t)
    if length==3:
        if t[2]=='text':
            r = makehtml.Text_Input(t[0])
        elif t[2]=='textarea':
            r = makehtml.Text_Input(t[0])
        elif t[2]=='title':
            r = makehtml.Static_Title(t[0])
    elif length==4:
        if t[3]=='select':
            val_len = len(t[0][0])
            options = []
            options.append(t[2])
            while val_len:
                val_len-=1
                values = t[0][val_len].values()
                options.append(values[1])
            print options
            r = makehtml.Select(options)
        elif t[3]=='radio':
            val_len = len(t[0][0])
            options = []
            options.append(t[2])
            while val_len:
                val_len-=1
                values = t[0][val_len].values()
                options.append(values[1])
            r = makehtml.Radio_Button(options)
        elif t[3] == 'checkbox':
            val_len = len(t[0][0])
            options = []
            options.append(t[2])
            while val_len:
                val_len-=1
                values = t[0][val_len].values()
                options.append(values[1])
            r = makehtml.Check_Box(options)
    return r
'''
DB Options
var3(t)
var1(t)
txt(t)
'''
def Get_Table(t):
    length = len(t)
    if length==3:
        if t[2]=='text':
            n = t[0].replace (" ", "_")
            r = makehtml.var3(n)
        elif t[2]=='textarea':
            n = t[0].replace (" ", "_")
            r = makehtml.txt(n)
        elif t[2]=='title':
            n = t[0].replace (" ", "_")
            r = makehtml.var3(n)
    elif length==4:
        if t[3]=='select':
            n = t[2].replace (" ", "_")
            r = makehtml.var1(n)
        elif t[3]=='radio':
            n = t[2].replace (" ", "_")
            r = makehtml.var1(n)
        elif t[3] == 'checkbox':
            n = t[2].replace (" ", "_")
            r = makehtml.var1(n)
    return r


#Here we get the HTML of the fields 
def Create_HTML(t):
    global html
    h = Get_Data(t)
    html +=h

#Here we get the data variables
def Create_Table(t):
    global table
    h = Get_Table(t)
    table +=h

array = sorted(array, key=getKey)
print "----------"
no_of_fields = len(array)
k = 0
while k < no_of_fields:
    Create_HTML(array[k])
    k+=1

tb = 1
while tb < no_of_fields:
    Create_Table(array[tb])
    tb+=1

table = table + "`fir` varchar(100) NOT NULL, `doc_no` varchar(100) NOT NULL, `pcode` varchar(100) NOT NULL, "
print table
#This is the name
name = array[0][0]
name = name.replace (" ", "_")
#Now extract all the names for the database
data = []
datalen = len(array)
da = 0
while da < datalen:
    if(len(array[da])==3):
        data.append(array[da][0])
    elif(len(array[da])==4):
        data.append(array[da][2])
    da+=1

'''
dbnew = MySQLdb.connect(host="localhost", 
                     user="opennirv_php", 
                      passwd="}wWkNzI6A-N7", 
                      db="opennirv_rma")
'''

html = makehtml.Body(data, html)
makehtml.CreateHTML(name, html)
makehtml.CreateTable(name, table)
makehtml.CreateHTMLlist(name)

'''
x = dbnew.cursor()
sql = "INSERT INTO rma_forms(`form`) VALUES('%s');"%(name.lower())
print sql
x.execute(sql)
dbnew.commit()
x.close()
'''

#print html
print "HTML Form Created"
#print table
print "----------"
print "End of Python Script"
