import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def sum(x, y):
        return str(x + y)

    num1 = browser.find_element(By.ID, "num1")
    x = int(num1.text)

    num2 = browser.find_element(By.ID, "num2")
    y = int(num2.text)

    z = sum(x, y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit_button.click()










finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()