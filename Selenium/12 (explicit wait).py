from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    button = browser.find_element(By.TAG_NAME, 'button')
    # Выполнение программы продолжится, как значение текста у id price станет '$100'
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button.click()

    x = browser.find_element(By.ID, 'input_value').text
    fill_in = browser.find_element(By.CLASS_NAME, 'form-control')
    fill_in.send_keys(calc(x))
    submit = browser.find_element(By.ID, 'solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()



finally:
    time.sleep(30)
    browser.quit()
