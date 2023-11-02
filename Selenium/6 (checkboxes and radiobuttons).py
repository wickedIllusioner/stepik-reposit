from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/math.html')

    fill_in = browser.find_element(By.CSS_SELECTOR, '#answer.form-control')
    x = browser.find_element(By.CSS_SELECTOR, 'span.nowrap#input_value').text
    fill_in.send_keys(calc(x))

    checkbox = browser.find_element(By.CSS_SELECTOR, '.form-check-input#robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, '.form-check-input#robotsRule')
    radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()

