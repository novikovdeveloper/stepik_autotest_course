import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("B")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("P")
    input3 = browser.find_element(By.CSS_SELECTOR, ".form-control.city")
    input3.send_keys("R")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("S")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла