import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By



try:
    link = " https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    field.send_keys(y)

    robot = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot.click()

    robots_rule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_rule.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
