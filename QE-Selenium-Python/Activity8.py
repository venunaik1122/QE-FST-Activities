from selenium.webdriver.common.by import By
import time
from selenium import webdriver

with webdriver.Firefox() as driver:
    
    actions = webdriver.ActionChains(driver)
    
    driver.get("https://training-support.net/webelements/mouse-events")
    
    print(driver.title)
    
    e1 = driver.find_element(By.XPATH, "//h1[text()='Cargo.lock']")
    #//d
    actions.click(e1).perform()
    
    time.sleep(3)
    
    e2 = driver.find_element(By.XPATH,"//div[@class ='file'] /div//h1[text() = 'Cargo.toml']")
    
    actions.move_to_element(e2).click(e2).perform()
    
    time.sleep(3)  
    
    print(e2.text) 
    
    e3 = driver.find_element(By.XPATH, "//h1[text() ='src']")
    actions.double_click(e3).perform()
    
    time.sleep(3)
    
    print(e3.text)
    
    e4 = driver.find_element(By.XPATH, "//h1[text() = 'target']")
    
    actions.context_click(e4).perform()
    
    print(e4.text)
    
    time.sleep(3)
    e4.click()
    e5=driver.find_element(By.XPATH,"//div[@class='h-full w-full svelte-1444rg7']/li/button/span[text()='open']")
    
    
    actions.click(e5).perform()
    
    time.sleep(3)
    
    print(e5.text)