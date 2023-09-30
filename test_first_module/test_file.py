import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Vasya")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Pupkin")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("pupkin@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_task.txt')
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()