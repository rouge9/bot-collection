from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "C:\dev\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://seo-blog-front-end.vercel.app/signup")


type_name = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div/form/div[1]/input')
type_name.send_keys("blabla")
type_email = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div/form/div[2]/input')
type_email.send_keys("blabla@gmail.com")
type_password = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div/form/div[3]/input')
type_password.send_keys("password")
type_password.send_keys(Keys.ENTER)




