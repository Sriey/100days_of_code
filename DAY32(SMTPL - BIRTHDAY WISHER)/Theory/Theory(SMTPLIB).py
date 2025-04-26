import smtplib

mail = "2205932@kiit.ac.in"
password = "urjztawqaddsepmi"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=mail, password=password)
connection.sendmail(from_addr=mail, to_addrs="opps123@myyahoo.com", msg="inhweipv\n\nHello Baby")
connection.close()