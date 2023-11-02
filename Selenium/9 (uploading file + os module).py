from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    fill_in = browser.find_elements(By.CLASS_NAME, 'form-control')
    for fill in fill_in:
        fill.send_keys('test')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'blank.txt')

    file_export = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    file_export.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()


finally:
    time.sleep(10)
    browser.quit()