from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    # Открытие ссылки в браузере
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    # Нажатие кнопки и принятие запроса alert
    launch = browser.find_element(By.TAG_NAME, 'button').click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, 'input_value').text
    fill_in = browser.find_element(By.CSS_SELECTOR, 'input.form-control')
    fill_in.send_keys(calc(x))
    submit = browser.find_element(By.TAG_NAME, 'button')
    submit.click()



finally:
    time.sleep(30)
    browser.quit()