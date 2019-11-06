from selenium import webdriver
import time



try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)


        input = browser.find_elements_by_css_selector("input:required")
        input[0].send_keys("Ivan")
        input[1].send_keys("Petrov")
        input[2].send_keys("ya@mail.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text


        assert "Congratulations! You have successfully registered!" == welcome_text
finally:
        time.sleep(10)
        browser.quit()