import cgi
form = cgi.FieldStorage()
username = form.getfirst("username")
password = form["password"].value
if username == "admin" and password == "admin1234":
    message = "Вхід успішно виконано"
else:
    message = "Вхід не успішний"

print(f"<h1>{message}</h1>")
