from selenium.webdriver.common.by import By
from selenium import webdriver

with webdriver.Firefox() as driver:
    actions = webdriver.ActionChains(driver)
    driver.get("https://training-support.net/webelements/mouse-events")
    
    
    print(driver.title)
    
    e1 = driver.find_element(By.XPATH, "//h1[@text='cargo.lock']")
    actions.click(e1)
    
    e2 = driver.find_element(By.XPATH, "//h1[@text='Cargo.toml']")
    actions.move_to_element(e2)
    
    e3 = driver.find_element(By.XPATH, "//h1[@text='Cargo.toml']")
    actions.click(e3)
    
    res = driver.find_element(By.ID, "result")
    print(res.text)
    
    