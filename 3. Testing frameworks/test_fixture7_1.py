import pytest, time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    print(lesson)
    browser.quit()

lesson = ''

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_partial_text(browser, number):
    global lesson
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    answer_field = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder~='answer']"))
    )
    answer = math.log(int(time.time()))
    answer_field.send_keys(str(answer))
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    hint = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='_hint']"))
    )
    result = hint.text
    if result != 'Correct!':
        lesson = f"{lesson}{result}"
    assert result == "Correct!", f"Expected: 'Correct!', got '{result}'"
