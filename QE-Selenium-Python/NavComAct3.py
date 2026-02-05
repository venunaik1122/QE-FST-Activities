from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/login-form")
    
    print(driver.title)
    
    ele1 =driver.find_element(By.XPATH,"//input[@id='username']")
    ele1.send_keys("admin")
    
    ele2 =driver.find_element(By.XPATH,"//input[@id='password']")
    
    ele2.send_keys("password")
    
    driver.find_element(By.XPATH,"//button[@class='svelte-1pdjkmx']").click()
    
    print(driver.title)
    
    driver.quit()
    
        
    