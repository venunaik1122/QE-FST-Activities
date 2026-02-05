import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Firefox() as driver:
     
     driver.get("https://training-support.net/webelements/drag-drop")
     
     print(driver.title)
     
     actions = webdriver.ActionChains(driver)
     
     e1 = driver.find_element(By.ID, "ball")
     drop1 = driver.find_element(By.XPATH, "//div[@id ='dropzone1']")
     drop2 = driver.find_element(By.XPATH, "//div[@id ='dropzone2']")
     
     drop1_status = driver.find_element(By.XPATH, "//div[@id ='dropzone1']//span[@class ='dropzone-text svelte-lit24y']")
     
     drop2_status = driver.find_element(By.XPATH, "//div[@id ='dropzone2']//span[@class ='dropzone-text svelte-lit24y']")
     
    
     status_1 = actions.click_and_hold(e1).drag_and_drop(e1,drop1).perform()
     time.sleep(3)
     
     print(drop1_status.text)
     
     actions.drag_and_drop(e1,drop2).perform()
     time.sleep(3)
     
     print(drop2_status.text)
     