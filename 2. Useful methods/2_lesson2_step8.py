import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    elements = browser.find_elements(By.CSS_SELECTOR, "[type='text']")
    a = 1
    for element in elements:
        element.send_keys('test' + str(a))
        a+=1

    file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '2_lesson2_step8.txt')    # добавляем к этому пути имя файла
    file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()