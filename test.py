import cgi

form = cgi.FieldStorage()

searchterm = form.getvalue('variable')
print(searchterm)