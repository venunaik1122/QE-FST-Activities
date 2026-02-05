import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/selects")
    
    # print(driver.title)
    
    # opt1 = Select(driver.find_element(By.XPATH , "//select[@class ='h-10 w-64 rounded-lg border-2 border-black bg-purple-200 px-3 shadow-md transition hover:shadow-lg']"))
    
    # opt1.select_by_visible_text("Two")
    # print("second option selected: ",opt1.first_selected_option.text)
    # time.sleep(3)
    
    # opt1.select_by_index(3)
    # print("third option selected: ",opt1.first_selected_option.text)
    # time.sleep(3)
    # opt1.select_by_value("four")
    # print("fourth option selected: ",opt1.first_selected_option.text)
    # time.sleep(3)
    # lis_options = opt1.options
    
    # for op in lis_options:
    #     print(op.text)
    
    
    ##mulitple select and deselect 
    
    multiple= Select(driver.find_element(By.XPATH, "//select[@class ='h-80 w-64 rounded-lg border-2 border-black bg-purple-200 p-3 shadow-md transition hover:shadow-lg focus:border-2 focus:border-black focus:ring-0']"))
    
    multiple.select_by_visible_text("HTML")
    multiple
    
    time.sleep(3)
    