#!C:/Python/python.exe
print("Content-Type: text/html\n")

import cgi

form = cgi.FieldStorage()

assignment_group = form.getvalue('assignment_group')
caller = form.getvalue('caller')
short_descr = form.getvalue('short_description')
descr = form.getvalue('description')

#TESTING
print("Assignment Group: " + assignment_group +"<br>")
print("Caller/Email: " + caller +"<br>")
print("Short Description: " + short_descr +"<br>")
print("Description: " + descr+"<br>")
