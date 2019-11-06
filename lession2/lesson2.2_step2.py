from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    sum_needle = int(browser.find_element_by_css_selector("#num1").text) + int(browser.find_element_by_css_selector("#num2").text)
    el_select = Select(browser.find_element_by_css_selector('#dropdown'))
    el_select.select_by_value(str(sum_needle))
    # Жмем кнопку submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
