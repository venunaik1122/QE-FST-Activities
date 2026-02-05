import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/alerts")
    
    print(driver.title)
    
    btn1 = driver.find_element(By.XPATH, "//button[@id ='simple']")
    btn1.click()
    
    alert1 = driver.switch_to.alert
    
    time.sleep(3)
    
    print(alert1.text)
    
    
    ##Activity 19
    btn2 = driver.find_element(By.XPATH, "//button[@id ='confirmation']")
    btn2.click()

    alert2 = driver.switch_to.alert
    
    time.sleep(3)
    print(alert2.text)
    alert2.accept()
    
    
    btn3 = driver.find_element(By.XPATH, "//button[@id ='confirmation']")
    btn3.click()

    alert3 = driver.switch_to.alert
    
    time.sleep(3)
    print(alert3.text)
    alert3.dismiss()
    
    print_txt = driver.find_element(By.XPATH, "//p[@id ='result']")
    
    print(print_txt.text)
    
    ##Activity20
    btn4 = driver.find_element(By.XPATH,"//button[@id='prompt']")
    btn4.click()
    alert5 = driver.switch_to.alert
    alert5.send_keys("hello")
    print(alert5.text)
    alert5.accept()
    
    
    
    
    
    
    
    
    
    
    