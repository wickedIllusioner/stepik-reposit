import time
from selenium import webdriver  # Набор команд для управления браузером
from selenium.webdriver.common.by import By     # Класс By позволяет выбрать способ поиска элемента


driver = webdriver.Chrome() # Открытие браузера Chrome (закрывается моментально)
time.sleep(1)   # Держит Chrome открытым на протяжении N секунд

driver.get('https://suninjuly.github.io/text_input_task.html')  # Драйвер получает запрос GET на открытие веб-страницы
time.sleep(0.5)

# Метод find_element ищет нужный элемент на сайте и указывает к нему путь
textarea = driver.find_element(By.CSS_SELECTOR, '.textarea')    # Метод принимает в качестве аргументов способ поиска и значение, по которому будет произведен поиск
textarea.send_keys('input-text') # Ввод текста ответа в найденное поле
time.sleep(0.5)

submit_button = driver.find_element(By.CSS_SELECTOR, '.submit-submission')  # Поиск кнопки, отправляющая введенное решение
submit_button.click()   # Нажатие кнопки
time.sleep(2)

driver.quit()   # Закрытие окна браузера (крайне рекомендуется делать после всех проделанных действий)