from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

with webdriver.Firefox() as driver:
    
    actions = webdriver.ActionChains(driver)
    
    driver.get("https://training-support.net/webelements/keyboard-events")
    
    print(driver.title)
    time.sleep(3)
    
    e1 =driver.find_element(By.XPATH,"//h1[@class ='mt-3 text-center text-4xl font-semibold text-black']")
    
    
    
    actions.click(e1).key_down(Keys.SHIFT).send_keys("S").key_up(Keys.SHIFT).send_keys("elenium").perform()
    print("Entered text: ",e1.text)  
    