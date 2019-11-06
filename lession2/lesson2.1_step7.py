from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Ищем родственный элемент input после label с заданым текстом (ось sibling)
    el = browser.find_element_by_css_selector("img#treasure")
    x = el.get_attribute('valuex')
    x = calc(int(x))

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(str(x))

    chkbox1 = browser.find_element_by_css_selector("#robotCheckbox")
    chkbox1.click()

    radioBtn = browser.find_element_by_css_selector("#robotsRule")
    radioBtn.click()
    
    # Жмем кнопку submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
