from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self, browser):
        self.browser = browser
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Не произошел переход на страницу логин"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Не отобразилась форма логина"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Не отобразилась форма регистрации"

    def register_new_user(self, email, password):
        email_reg = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        email_reg.send_keys(email)
        pass_reg = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS_FIELD)
        pass_reg.send_keys(password)
        repeat_pass = self.browser.find_element(*LoginPageLocators.REGISTRATION_REPEAT_PASS_FIELD)
        repeat_pass.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTRATION_BTN)
        reg_btn.click()




