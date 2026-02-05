from selenium.webdriver.common.by import By
from selenium import webdriver

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/dynamic-controls")
    
    print(driver.title)
    
    e1 = driver.find_element(By.XPATH,"//input[@'checkbox']")
    
    print(e1.is_displayed())
    
    print(e1.is_enabled())
    
    e2=driver.find_element(By.XPATH,"//button[@class='svelte-sfj3o4']")
    e2.click()
    
    print(f"check the checkbox is selected or not ? {e2.is_enabled} or not")
    print()