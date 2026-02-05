from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    
    driver.get("https://training-support.net/webelements/tables")
    
    print(driver.title)
    
    cols = driver.find_elements(By.XPATH, "//table/thead/tr/th")
    print(len(cols))
    
    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
    print(len(rows))
    
    third_row = driver.find_element(By.XPATH,"//table/tbody/tr[3]")
    
    print(third_row.text)
    
    s_r_s_c = driver.find_element(By.XPATH, "//table/tbody/tr[2]/td[2]")
    
    print(s_r_s_c.text)