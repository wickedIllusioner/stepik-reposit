from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select    # Импортируем класс Select для работы со списками 
import time


def get_sum(n1, n2):
    return str(int(n1) + int(n2))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects2.html')

    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    result = get_sum(num1, num2)

    # Переменной select присваиваем значение класса Select, в котором ищем элемент по тегу select
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(result)  # Выбираем найденную сумму в списке и кликаем на нее
    time.sleep(1)

    submit_button = browser.find_element(By.CLASS_NAME, 'btn')
    submit_button.click()


finally:
    time.sleep(30)
    browser.quit()