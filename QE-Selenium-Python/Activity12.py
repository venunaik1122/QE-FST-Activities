import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Firefox() as driver:
    
    wait = WebDriverWait(driver,10)
    
    driver.get("https://training-support.net/webelements/dynamic-content")
    
    print(driver.title)
    
    btn = driver.find_element(By.XPATH, "//button[@id='genButton']")
    
    btn.click()
    
    
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//h2[@id ='word']"),"release"))
    
    e2 = driver.find_element(By.XPATH, "//h2[@id ='word']")
    print("element found: ",e2.text)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    