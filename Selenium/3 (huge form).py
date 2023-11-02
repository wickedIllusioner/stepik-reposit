import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/huge_form.html')

    fields = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for field in fields:
        field.send_keys('Test Value')
    
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()