from selenium import webdriver
import time


chrome_driver_path = "D:\pythonProject\othersoft\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")
cookie_money = driver.find_element_by_id("money")

# upgeade_list = driver.find_elements_by_class_name("grayed")
# upgeade_list.reverse()

upgeade_list=[
    '//*[@id="buyElder Pledge"]',
    '//*[@id="buyTime machine"]',
    '//*[@id="buyPortal"]',
    '//*[@id="buyAlchemy lab"]',
    '//*[@id="buyShipment"]',
    '//*[@id="buyMine"]',
    '//*[@id="buyFactory"]',
    '//*[@id="buyGrandma"]',
    '//*[@id="buyCursor"]'
]



zz = driver.find_element_by_xpath('//*[@id="cps"]')
print(zz.text)

timeout = time.time() + 5 * 60
checkpoint = time.time()
game_go = True
while game_go:
    cookie.click()


    if time.time() > timeout:
        game_go = False
        zz = driver.find_element_by_xpath('//*[@id="cps"]')
        print(zz.text)
        timeout = time.time() + 5 * 60

    if time.time() - checkpoint > 13:
        for item in upgeade_list:
            upgrade=driver.find_element_by_xpath(item)
            is_available = upgrade.get_attribute("class")

            if is_available != "grayed":
                upgrade.click()
                break

        checkpoint = time.time()

# driver.close()
