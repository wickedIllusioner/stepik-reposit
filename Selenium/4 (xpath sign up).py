import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_xpath_form')

    fields = browser.find_elements(By.XPATH, '//input[@type="text"]')
    for field in fields:
        field.send_keys('Test Value')
    
    submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]') # Поиск кнопки по её тексту
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()