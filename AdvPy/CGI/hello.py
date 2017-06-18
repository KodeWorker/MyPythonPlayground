#! C:\Users\IRTI\Anaconda3\python.exe

import cgi

print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<title> CGI example </title>')
print('<body>')
print('<h1> Hello Program! </h1>')

form = cgi.FieldStorage()
if form.getvalue('name'):
    name = form.getvalue('name')
    print('<h2> Hello ' + name + '! Thanks for using the script!</h2> <br />')

if form.getvalue('happy'):
    print('<p>Yay! :D </p>')
if form.getvalue('sad'):
    print('<p>Why! :( </p>')

print('<form method="post" action="hello.py">')
print('<p> Name: <input type="text" name="name" /></p>')
print('<input type="checkbox" name="happy" /> HAPPY')
print('<input type="checkbox" name="sad" /> SAD')
print('<input type="submit" value="Submit" />')
print('</form>')

print('</body></html>')