from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def scroll(obj):
    browser.execute_script("return arguments[0].scrollIntoView(true);", obj)

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    scroll(answer)
    answer.send_keys(y)

    check = browser.find_element(By.ID, "robotCheckbox")
    scroll(check)
    check.click()

    radio = browser.find_element(By.ID, "robotsRule")
    scroll(radio)
    radio.click()

    button = browser.find_element_by_tag_name("button")
    scroll(button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
