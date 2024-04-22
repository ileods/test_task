import string
import random


class Base:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return str(rand_string)

    def assert_word(self, word, result):
        value_word = word.text.split(':')[1]
        assert value_word == result
        print("good value word: " + result)
