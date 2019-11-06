from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_css_selector('#input_value').text
    x = calc(x)
    el = browser.find_element_by_css_selector("#answer")
    el.send_keys(x)
    el = browser.find_element_by_css_selector('#robotCheckbox')
    el.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);",el)
    el = browser.find_element_by_css_selector('#robotsRule')
    el.click()
    # Жмем кнопку submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
