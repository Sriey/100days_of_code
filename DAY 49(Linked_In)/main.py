from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

email = "coder.100daysofcode@gmail.com"
security = "M3wNGg.AL6p;az&"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/feed/")

username = driver.find_element(By.ID, value="username")
password = driver.find_element(By.ID, value="password")
username.send_keys(email)
password.send_keys(security,Keys.ENTER)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4112887343&f_AL=true&geoId=&keywords=Python%20Developer&location=India&origin=JOB_SEARCH_PAGE_JOB_FILTER")

apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

Easy_apply = driver.find_element(by=By.CLASS_NAME, value="artdeco-text-input--input")
Easy_apply.send_keys("9348938756")
