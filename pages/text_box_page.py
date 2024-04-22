from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_class import Base


class Text_box_page(Base):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url
        self.name = self.generate_random_string(6)
        self.email = self.generate_random_string(5) + '@' + self.generate_random_string(4)+'.' + self.generate_random_string(2)
        self.current_address = self.generate_random_string(20)
        self.permanent_address = self.generate_random_string(20)


    # Locators
    full_name_locator = "//input[@id='userName']"
    email_locator = "//input[@id='userEmail']"
    current_address_locator = "//textarea[@id='currentAddress']"
    permanent_address_locator = "//textarea[@id='permanentAddress']"
    submit_locator = "//button[@id='submit']"
    full_name_result_locator = "//p[@id='name']"
    email_result_locator = "//p[@id='email']"
    current_address_result_locator = "//p[@id='currentAddress']"
    permanent_address_result_locator = "//p[@id='permanentAddress']"

    # Getters
    def get_full_name_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.full_name_locator)))

    def get_email_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_locator)))

    def get_current_address_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.current_address_locator)))

    def get_permanent_address_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.permanent_address_locator)))

    def get_submit_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_element(By.XPATH, self.submit_locator))
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submit_locator)))

    def get_full_name_result_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.full_name_result_locator)))

    def get_email_result_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_result_locator)))

    def get_current_address_result_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.current_address_result_locator)))

    def get_permanent_address_result_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.permanent_address_result_locator)))

    # Actions
    def input_full_name(self, name):
        self.get_full_name_input().send_keys(name)
        print("send name")

    def input_email(self, email):
        self.get_email_input().send_keys(email)
        print("input email")

    def input_current_address(self, current_address):
        self.get_current_address_input().send_keys(current_address)
        print("input current address")

    def input_permanent_address(self, permanent_address):
        self.get_permanent_address_input().send_keys(permanent_address)
        print("input permanent address")

    def click_submit(self):
        self.get_submit_button().click()
        print("click submit")

    # Methods
    def input_form(self):
        self.input_full_name(self.name)
        self.input_email(self.email)
        self.input_current_address(self.current_address)
        self.input_permanent_address(self.permanent_address)

    def send_form(self):
        self.click_submit()

    def check_result(self):
        self.assert_word(self.get_full_name_result_text(), self.name)
        self.assert_word(self.get_email_result_text(), self.email)
        self.assert_word(self.get_current_address_result_text(), self.current_address)
        self.assert_word(self.get_permanent_address_result_text(), self.permanent_address)