from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    
    driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
    
    
    print(driver.title)
    
    checkboxs = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
    
    for checkbox in checkboxs :
        checkbox.click()
    