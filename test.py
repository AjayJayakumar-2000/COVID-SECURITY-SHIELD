import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('projectg287@gmail.com','ajay221200')
test_list = ['ajayjayakumar2000@gmail.com', 'node.js API ', 'ajayjayakumar2000@gmail.com']
print("The original list is : " + str(test_list))

res = []
for i in test_list:
    if i not in res:
        res.append(i)

# printing list after removal 
print("The list after removing duplicates : " + str(res))
print(res)
for j in res:

    server.sendmail('projectg287@gmail.com', j, 'your son absent today')
    print("mail send")
