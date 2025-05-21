from selenium import webdriver
from selenium.webdriver.common.by import By
import time

starting_time = time.time()
t_end = time.time() + (60 * 2)
next_check_time = starting_time + 10
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

attribute_ids = [item.get_attribute("id") for item in driver.find_elements(By.CSS_SELECTOR, "#store div")]
attribute_ids = attribute_ids[::-1]
def check_attribute_panel():
    for attribute in attribute_ids:
        item_details = driver.find_element(By.ID, attribute)
        if item_details.get_attribute("class") == "":
            item_details.click()
            break
        else:
            pass


while time.time() < t_end:
    if time.time() > next_check_time:
        check_attribute_panel()
        next_check_time += 10
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()



if time.time() > t_end:
    cookies_per_second = driver.find_element(By.CSS_SELECTOR, "#saveMenu #cps").text
    print(cookies_per_second)
