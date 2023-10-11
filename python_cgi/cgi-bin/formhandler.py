import cgi
import html
import http.cookies
import os

form = cgi.FieldStorage()

try:
    username = form.getfirst("username", "admin")
    password = form.getfirst("password", "")
    username = html.escape(username)
    password = html.escape(password)
   
    lang = form.getvalue("lang", "не обрано мову")

    groups = ["ipz31", "ipz32", "ipz33"]
    groups_checkbox = {}
    for group in groups:
        value_choice = form.getvalue(group, "off")
        groups_checkbox[group] = value_choice
       
    if username == "admin" and password == "admin1234":
        message = "вхід виконано успішно"
    else:
        message = "вхід не успішний, перевірте дані входу"

except (NameError, KeyError) as e:
    message = "введіть дані для форми"
    lang = None
    print(message)
    
print(f"Set-cookie: name={username};")
print(f"Set-cookie: password={password[0]};")

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name_cookie = cookie.get("name").value
password_cookie = cookie.get("password").value

print("Content-type:text/html\r\n\r\n")

template_html = f"""
<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Обробка форми</title>
</head>
<body>
    <h1> Hi, {username} </h1>
    <h1> {message} </h1>
    <h2> {groups_checkbox=} </h2>
    <h3> {os.environ["HTTP_COOKIE"]=} </h3>
    <h3> From cookie: {name_cookie=} {password_cookie=} </h3>
</body>
</html>
"""
print(template_html)





