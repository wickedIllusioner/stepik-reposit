from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')

    fill_in = browser.find_element(By.CSS_SELECTOR, '#answer.form-control')
    x = browser.find_element(By.CSS_SELECTOR, 'span.nowrap#input_value').text
    fill_in.send_keys(calc(x))

    checkbox = browser.find_element(By.CSS_SELECTOR, '.form-check-input#robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, '.form-check-input#robotsRule')
    
    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)  # execute_script выполняет скрипт, написанный на JavaScript
    # В данном случае скрипт перемещает пользователя в видимую зону кнопки submit_button для возможности нажать на нее
    radiobutton.click()
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()