from selenium import webdriver
with webdriver.Chrome() as driver:
    driver.get("https://training-support.net")
    
    print(driver.title)
    
    driver.quit()