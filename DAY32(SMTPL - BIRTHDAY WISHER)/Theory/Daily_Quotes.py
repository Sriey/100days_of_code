import smtplib,datetime,random

#reading all the Quotes As a list
with open("quotes.txt") as file:
    quotes = file.readlines()

#Saving the Sender's Mail and App Password
mail = "2205932@kiit.ac.in"
password = "urjztawqaddsepmi"

#Getting The Current Day
now = datetime.datetime.now()
day = now.weekday()

#Choosing Day As wednesday  (Here 2 represents Wednesday as Monday is 0)
if day == 2:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=mail,password=password)
    quote = random.choice(quotes)
    connection.sendmail(from_addr=mail,to_addrs="shiwanshshukla25@gmail.com",msg=f"subject:Quotes\n\n{quote}")
    connection.close()
