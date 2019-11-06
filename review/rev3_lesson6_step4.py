from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

   

    first = browser.find_element_by_class_name("first")
    first.send_keys("Ivan")
    second = browser.find_element_by_class_name(".second")
    second.send_keys("Petrov")
    third = browser.find_element_by_class_name(".third")
    third.send_keys("artanovo@gmail.com")
    browser.find_element_by_css_selector
    first.cromexPathFinder = browser.find_element_by_class_name("first.cromexPathFinder")
    first.cromexPathFinder.send_keys("artanovo@gmail.com")
    second.cromexPathFinder = browser.find_element_by_class_name("second.cromexPathFinder")
    second.cromexPathFinder.send_keys("artanovo@gmail.com")	

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    
    welcome_text = welcome_text_elt.text

   
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
   
    time.sleep(10)
   
    browser.quit()