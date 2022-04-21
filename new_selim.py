from selenium import webdriver

chrome_driver_path = "C:\dev\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")
# link = driver.find_element_by_css_selector(".documentation-widget a")
# for n in link:
#     print(n.text)

# events = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
# upcoming_dict = {
#     "key": "event"
# }
# print(events[0].text)

time = driver.find_elements_by_css_selector(".event-widget time")
name = driver.find_elements_by_css_selector(".event-widget li a")

events = {}

for n in range(len(time)):
    events[n] = {
        "time":time[n].text,
        "name":name[n].text
    }

print(events)

driver.quit()