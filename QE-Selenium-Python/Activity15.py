
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/dynamic-attributes")
    
    print(driver.title)
     
    # input1 = driver.find_element(By.XPATH, "//input[startswith(@id='full-name')]")
    
    ##By using CSS selector
    input1 = driver.find_element(By.CSS_SELECTOR, "input[id^='full-name']")
    input1.send_keys("venu")
    
    ##by using CSS selector
    # m1 = driver.find_element(By.XPATH, "//input[@id$ = 'email']")
    
    m1 = driver.find_element(By.CSS_SELECTOR, "input[id$='email']")
    
    m1.send_keys("Venunaik121@gmail.com")
    
    ##by using CSS selector
    # dates = driver.find_element(By.XPATH, "//input[@type ='date']")
    dates = driver.find_element(By.CSS_SELECTOR, "input[name*='event-date']")
    
    dates.send_keys("2026-02-02")
    
    additional_info = driver.find_element(By.XPATH, "//textarea[@class ='focus:ring-0 svelte-7bqce9']")
    
    additional_info.send_keys("Nothing")
    
    btn = driver.find_element(By.XPATH, "//button[@class ='font-bold svelte-7bqce9']")
    
    btn.click()
    time.sleep(3)
    
    status = driver.find_element(By.XPATH, "//h3[@id='action-confirmation']")
    print("status: ",status.text)