from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

date = driver.find_elements(By.CSS_SELECTOR, value='#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul time')
name = driver.find_elements(By.CSS_SELECTOR, value='#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul li a')

dict = {}
for i in range(len(name)):
    dict[i] = {
        "Date" : date[i].text,
        "Name": name[i].text
        }

print(dict)

driver.close()
email = "coder.100daysofcode@gmail.com"
security = "M3wNGg.AL6p;az&"
