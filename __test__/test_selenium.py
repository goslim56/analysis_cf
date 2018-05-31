import time
from selenium import webdriver

wd = webdriver.Chrome('D:/cafe24/python/webdriver/chromedriver.exe')
wd.get('http://www.cafe24.com')
time.sleep(10)

html = wd.page_source
print(html)

wd.quit()
