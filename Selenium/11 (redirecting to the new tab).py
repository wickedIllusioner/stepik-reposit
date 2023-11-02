from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    initial_window = browser.window_handles[0]
    button = browser.find_element(By.TAG_NAME, 'button').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value').text
    fill_in = browser.find_element(By.CSS_SELECTOR, 'input.form-control')
    fill_in.send_keys(calc(x))
    submit = browser.find_element(By.TAG_NAME, 'button')
    submit.click()



finally:
    time.sleep(30)
    browser.quit()
