import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def convert(a):
    b = ""
    c = ""
    for z in a:
        if 48 <= ord(z) <= 57:
            b += z
        else:
            c += z
    return [int(b),c]

def check():
    temp = driver.find_element(By.ID, value="money").text
    values = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    print(int(temp),values[0].text)
    for z in range(len(values)-2,-1,-1):
        t = convert(values[z].text)
        if int(temp) > t[0]:
            print("buy"+f"{t[1][0:len(t[1])-2]}")
            return


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

timeout = time.time() + 3
five_min = time.time() + 60*5

while True:
    cookie.click()
    if time.time() > timeout:
        check()
        timeout = time.time() + 3
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
