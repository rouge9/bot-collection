from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "C:\dev\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_num = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
print(article_num.text)

link = driver.find_element_by_link_text("April 21")
link.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()