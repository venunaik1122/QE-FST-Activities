import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    driver.implicitly_wait(10)
    
    driver.get("https://training-support.net/webelements/dynamic-controls")
    
    print(driver.title)
    actions = webdriver.ActionChains(driver)
    
    e1 = driver.find_element(By.XPATH, "//input[@id ='checkbox']")
    print("Status of checkbox: ",e1.is_displayed())
    print("Status of checkbox: ",e1.is_enabled())
    
    
    toggle_btn = driver.find_element(By.XPATH, "//button[@class ='svelte-sfj3o4']")
    
    toggle_btn.click()
    time.sleep(3)
    
    toggle_btn.click()
    time.sleep(3)
    e1.click()
    time.sleep(3)
    print(e1.text)
    
    
    
    
    
    