import time

from selenium import webdriver

# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://ful.io/')
time.sleep(10)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)

facebook = driver.find_element("xpath", "//a[@class='px-1']")
linkedin = driver.find_element("xpath", "//a[@href='https://www.linkedin.com/company/ful-io/']")
print("Social Links -")
print(facebook.get_attribute("href"))
print(linkedin.get_attribute("href"))
print()
time.sleep(10)

email = driver.find_element("xpath", "//a[normalize-space()='support@ful.io']")
print("Email/s-")
print(email.text)
print()
time.sleep(10)

contact = driver.find_element("xpath", "//a[normalize-space()='+1 343 303 6668']")
print("Contact:")
print(contact.text)
time.sleep(10)

driver.close()
