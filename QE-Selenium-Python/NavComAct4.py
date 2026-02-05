from selenium.webdriver.common.by import By
from selenium import webdriver

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/target-practice")
    
    print(driver.title)
    
    ele1 =driver.find_element(By.XPATH, "//h3[@class ='text-3xl font-bold text-orange-600']")
    print(ele1.text)
    
    ele2 =driver.find_element(By.XPATH, "//h5[@class ='text-3xl font-bold text-purple-600']")
    print(ele2.value_of_css_property("color"))
    
    
    ele3 = driver.find_element(By.XPATH, "//button[@class ='rounded-xl bg-purple-200 p-2 text-3xl font-bold text-purple-900 svelte-2hb4ib']")
    print(ele3.get_attribute("class"))
    
    ele4 =driver.find_element(By.CLASS_NAME,"rounded-xl bg-slate-200")
    print(ele4.text)
    
    
    
    driver.quit()