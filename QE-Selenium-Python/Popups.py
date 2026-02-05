import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/popups")
    
    print(driver.title)
    
    btn1 = driver.find_element(By.XPATH, "//button[@id='launcher']")
    
    btn1.click()
    
    username = driver.find_element(By.XPATH, "//input[@type ='text']")
    username.send_keys("admin")
    
    pwd = driver.find_element(By.XPATH, "//input[@type ='password']")
    pwd.send_keys("password")
    
    btn = driver.find_element(By.XPATH, "//button[@class ='svelte-1pdjkmx']")
    time.sleep(3)
    btn.click()
    
    status = driver.find_element(By.XPATH, "//h1[@class ='text-center font-display text-6xl font-bold text-emerald-500']")
    
    print("login status: ",status.text)