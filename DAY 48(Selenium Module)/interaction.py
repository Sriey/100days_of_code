from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

search = driver.find_elements(By.CLASS_NAME, value="form-control")

j = 0
for i in search:
    j += 1
    if j == 1:
        i.send_keys("Shiwansh")
    elif j == 2:
        i.send_keys("Shukla")
    else:
        i.send_keys("2205932@kiit.ac.in", Keys.ENTER)

