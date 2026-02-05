from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    
    driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
    
    
    print(driver.title)
    
    ford_opt = driver.find_element(By.ID,"option1")
    if not ford_opt.is_selected :
        ford_opt.click()

    bmw_opt = driver.find_element(By.ID,"option2")
    if not bmw_opt.is_selected:
        bmw_opt.clik()
    
    print("ford selected: " ,ford_opt.is_selected())
    print("bmw selected: " ,bmw_opt.is_selected())
    