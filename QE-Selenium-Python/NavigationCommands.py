from selenium import webdriver
with webdriver.Firefox() as driver:
    driver.get("https://training-support.net")
    
    print(driver.title)
    
    ele = driver.find_element(By.LINK_TEXT,"About Us")
    ele.click()
    print(driver.title)
    
    driver.quit()