import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

with webdriver.Firefox() as driver:
    
    driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
    
    
    print(driver.title)
    
    dropdown = Select(driver.find_element(By.ID,"carBrands"))
    
    dropdown.select_by_value("audi")
    
    print("selected :",dropdown.first_selected_option.text)
    
    dropdown.select_by_index(1)
    
    print("selected :",dropdown.first_selected_option.text)
    
    dropdown.select_by_visible_text("Mercedes")
    
    print("selected :",dropdown.first_selected_option.text)
    