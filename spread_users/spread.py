'''I have created new users in mikrotik and I want to send username and password in telegram in specific format so I wrote this script.'''

import re
try:
    file = open("users2.txt" , 'r')
    text = file.read()
    result = re.findall('name=.*password=.....'  ,  text)
    file.close()
except:
    print("error")
users = {}
for item in result:
    user , password = item.split(' ')
    user = user.split('=')[1]
    password = password.split('=')[1]
    users[user] = password
try:
    file = open('users-final.txt' , 'w+')
    for user , passw in users.items():
        file.write(f"user: {user}\npass: {passw}\n\n")
    file.close()
except:
    print("error")



print(users)