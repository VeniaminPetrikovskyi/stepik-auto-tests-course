import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")

    x1 = browser.find_element(By.ID, "num1").text
    x2 = browser.find_element(By.ID, "num2").text
    x = int(x1)+int(x2)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(x))
    submit = browser.find_element(By.CSS_SELECTOR, ".btn").click()
finally:
    time.sleep(10)
    browser.quit()
