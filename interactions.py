from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\pythonProject\othersoft\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# number_of_articles = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# print(number_of_articles.text)
# number_of_articles.click()

# all_portals=driver.find_element_by_link_text("All portals")
# all_portals.click()

# search_bar=driver.find_element_by_name("search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

login=driver.find_element_by_name("fName")
login.send_keys("Name")
login2=driver.find_element_by_name("lName")
login2.send_keys("Surname")
mail=driver.find_element_by_name("email")
mail.send_keys("mymail@gmail.com")
button=driver.find_element_by_css_selector("form button")
button.click()

# driver.close()


