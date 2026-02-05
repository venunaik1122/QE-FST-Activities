from os import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


with webdriver.Firefox() as driver:
    
    driver.get("https://training-support.net/webelements/tabs")
    
    wait =webdriver
    
    print("current window title: ",driver.title)
    
    original_handle = driver.current_window_handle
    print("Current table is: ",original_handle)
    
    btn = driver.find_element(By.XPATH,"//button[text()='Open A New Tab']")
    
    btn.click()
    
    wait.until(EC.new_window_is_opened(2))
    
    driver.switch_t  
    
    
    