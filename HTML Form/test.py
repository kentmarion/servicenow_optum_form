print "Content-type: text/html\n\n";

import cgi

form = cgi.FieldStorage()

assignment_group = form.getvalue('assignment_group')
caller = form.getvalue('caller')
short_descr = form.getvalue('short_description')
descr = form.getvalue('description')

#TESTING
print assignment_group
print caller
print short_descr
print descr
