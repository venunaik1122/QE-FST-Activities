from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    
    driver.get("https://training-support.net/webelements/tables")
    
    print(driver.title)
    
    cols = driver.find_elements(By.XPATH, "//table/thead/tr/th")
    print("rows: ",len(cols))
    
    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
    print("columns: ",len(rows))
    
    book = driver.find_element(By.XPATH,"//table/tbody/tr[5]/td[2]")
    
    print("5th row book name: ",book.text)
    
    
    price = driver.find_element(By.XPATH,"//table/thead/tr/th[5]")
    
    price.click()
    
    book5 = driver.find_element(By.XPATH,"//table/tbody/tr[5]/td[2]")
    
    print("After ascending 5th book: ",book5.text)
    
    
    
    
    
    
    
    