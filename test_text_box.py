import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.text_box_page import Text_box_page


def test_input_and_send_form():
    driver = webdriver.Chrome(
        service=ChromeService(executable_path='/Users/A/PycharmProjects/test_task/chromedriver'))
    url = "https://demoqa.com/text-box"
    tb_page = Text_box_page(driver, url)
    tb_page.open()
    tb_page.input_form()
    tb_page.send_form()
    tb_page.check_result()