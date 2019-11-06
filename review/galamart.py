from selenium import webdriver
import time

try:
    # link = "http://suninjuly.github.io/registration1.html"
    link = "https://galamart.ru/catalog/instrumenty/elektroinstrument-4vxfrad/akkumulyatornyy-instrument-3zzxrad/"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector(".sort-selected")
    input1.click()
    input2 = browser.find_element_by_xpath("//a[contains(text(),'дешевые')]")
    input2.click()
 

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
