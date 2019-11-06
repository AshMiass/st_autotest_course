from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    name_el = browser.find_element_by_css_selector('input[name="firstname"]')
    name_el.send_keys('I')
    surname_el = browser.find_element_by_css_selector('input[name="lastname"]')
    surname_el.send_keys('Van')
    email_el = browser.find_element_by_css_selector('input[name="email"]')
    email_el.send_keys('t@s.t')
    
    filename = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(filename, 'test.txt')
    print(filename)
    file_el = browser.find_element_by_css_selector('#file')
    file_el.send_keys(filename)
    # Жмем кнопку submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
