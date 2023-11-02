import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_link_text')

    hidden = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element(By.LINK_TEXT, hidden)   # Поиск ссылки по тексту ссылки переменной hidden
    link.click()

    data = ['Artyom', 'Veselov', 'Irkutsk', 'Russia']
    fill_in_areas = browser.find_elements(By.CLASS_NAME, 'form-control')    # Поиск нескольких полей ввода (fill_in_areas - список)
    for i in range(len(fill_in_areas)):
        fill_in_areas[i].send_keys(data[i])

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn')   # Поиск кнопки по классу btn
    submit_button.click()   # Нажатие кнопки


finally:
    time.sleep(10)
    browser.quit()