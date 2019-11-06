from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Ищем родственный элемент input после label с заданым текстом (ось sibling)
    # Имя
    input1 = browser.find_element_by_xpath("//label[contains(text(),'First name')]//following-sibling::input")
    input1.send_keys("I")
    # Фамилия
    input2 = browser.find_element_by_xpath("//label[contains(text(),'Last name')]//following-sibling::input")
    input2.send_keys("Van")
    # Email
    input3 = browser.find_element_by_xpath("//label[contains(text(),'Email')]//following-sibling::input")
    input3.send_keys("t@e.st")
    # Жмем кнопку submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
