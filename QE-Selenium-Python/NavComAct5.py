from selenium.webdriver.common.by import By
from selenium import webdriver

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/dynamic-controls")
    
    print(driver.title)
    
    e1 = driver.find_element(By.XPATH,"//input[@id='checkbox']")
    print(e1.is_displayed())
    
    e2=driver.find_element(By.XPATH,"//button[@class='svelte-sfj3o4']")
    e2.click()
    
    print(e1.is_displayed())
    
    
    
    
    
    
    
    