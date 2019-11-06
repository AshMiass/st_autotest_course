from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.webdriver.common.by import By
import time 
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    price_id = 'price'
    price_el = WebDriverWait(browser, 12).until(
      EC.text_to_be_present_in_element, By.id(price_id), < 100
    )
    print("price_el", price_el.text)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    second_tab = browser.window_handles[1]
    browser.switch_to.window(second_tab)

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
