#!/usr/bin/env python3


print("Content-type: text/html")
print()

import cgi 

# получим nick, введенный в форме
our_form = cgi.FieldStorage()
nick = our_form.getfirst("nick",'Незнайомець')

# сохраним в переменную  nameslist текст из файла names.txt
with open("names.txt", 'r',-1,'utf-8') as n:
  list=n.readlines()
  nameslist=[]
  for i in list:
    nameslist.append(i.strip())

# определим есть ли этот ник в файле names.txt 
if str(nick) in nameslist:
  print("Вже бачилися, "+nick+"!")
else:
  print("Привiт, "+nick+"!"+" Приємно познайомитися!")
  with open("names.txt", 'a',-1,'utf-8') as names:
    names.write(nick +"\n")



 