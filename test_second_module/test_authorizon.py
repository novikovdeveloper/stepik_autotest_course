import time
import math
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class TestAuth:
    def test_authorizon(self, browser, links):
        browser.get(links)
        enter = browser.find_element(By.ID, "ember33")
        enter.click()

        wait_modal = WebDriverWait(browser, 10).until(EC.presence_of_element_located
                                                   ((By.CSS_SELECTOR, ".light-tabs.ember-view")))

        login_field = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
        login_field.send_keys("mailforworkinbeeline@gmail.com")

        pass_field = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
        pass_field.send_keys("Test112233445566")

        submit_button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader")
        time.sleep(4)
        submit_button.click()
        dont_wait_modal = WebDriverWait(browser, 10).until_not(EC.presence_of_element_located
                                                               ((By.ID, ".light-tabs.ember-view")))

        WebDriverWait(browser, 20).until(EC.presence_of_element_located
                                         ((By.CSS_SELECTOR, ".ember-text-area.string-quiz__textarea")))
        time.sleep(10)
        text_area = browser.find_element(By.CSS_SELECTOR, ".ember-text-area.string-quiz__textarea")
        answer = str(math.log(int(time.time())))
        text_area.send_keys(answer)

        submit_button_question = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
        submit_button_question.click()

        feedback_text = browser.find_element(By.CSS_SELECTOR, ".smart-hints.lesson__hint").text
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints.lesson__hint")))

        assert feedback_text == "Correct!", "Текст в фидбеке не совпадает с ожидаемым"




