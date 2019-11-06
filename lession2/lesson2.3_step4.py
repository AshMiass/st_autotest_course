from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    el = browser.find_element_by_css_selector('#input_value')
    x = calc(el.text)
    browser.find_element_by_css_selector("#answer").send_keys(x)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    print(browser.switch_to.alert.text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
