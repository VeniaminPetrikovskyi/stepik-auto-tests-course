import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    submit = browser.find_element(By.CSS_SELECTOR, ".btn").click()
finally:
    time.sleep(10)
    browser.quit()
