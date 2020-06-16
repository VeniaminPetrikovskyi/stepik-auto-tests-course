import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element(By.ID, "answer").send_keys(y)

    check = browser.find_element(By.ID, "robotCheckbox").click()
    radio = browser.find_element(By.ID, "robotsRule").click()
    submit = browser.find_element(By.CSS_SELECTOR, ".btn").click()
finally:
    time.sleep(10)
    browser.quit()
