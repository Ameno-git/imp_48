import selenium
from bs4 import BeautifulSoup
from selenium import webdriver

chrome_driver_path = "D:\pythonProject\othersoft\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

event_dictionary = {}
driver.get("https://www.python.org/")
for line in range(5):
    element = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{line + 1}]')
    event_time = element.find_element_by_tag_name("time").get_attribute("datetime")[0:10]
    event_name = element.find_element_by_tag_name("a").text
    event_dictionary[line] = {
        "time": f"{event_time}",
        "name": f"{event_name}"
    }
    print(event_time, event_name)

test_time = driver.find_elements_by_css_selector(".event-widget time")
for time in test_time:
    print(time.text)

print(event_dictionary)

driver.close()
