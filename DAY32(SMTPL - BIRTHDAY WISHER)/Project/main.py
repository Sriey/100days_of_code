import smtplib,pandas,datetime

##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

mail = "2205932@kiit.ac.in"
password = "yusv cfry qtfs opiv"

now = datetime.datetime.now()
day = now.day
mth = now.month

file = pandas.read_csv("birthdays.csv")
days = file["day"].to_list()
months = file["month"].to_list()

if day in days and mth in months:
    print("yes")
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=mail,password=password)

    d = file[file.day == day]
    email = d[d.month == mth]
    for mal in email.iterrows():
        with open("letter_templates/letter_1.txt", mode="r") as letter:
            temp = letter.readlines()
            name = mal[1]["name"]
            temp[0] = temp[0].replace("[NAME]",name)
            print(temp)
        connection.sendmail(from_addr=mail,to_addrs=mal[1]["email"],msg=f"subject:Birthday Wish\n\n{"".join(temp)}")
    connection.close()