import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    first_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    first_button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    field.send_keys(y)

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit_button.click()


finally:
    time.sleep(10)
    browser.quit()