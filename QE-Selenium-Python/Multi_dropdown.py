import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

with webdriver.Firefox() as driver:

    # Open the webpage
    driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
    print("Page Title:", driver.title)

    # Locate the multi-select dropdown
    multi_dropdown = Select(driver.find_element(By.ID, "multiSelect"))

    # Check if multiple selection is supported
    if multi_dropdown.is_multiple:
        print("Dropdown supports multiple selection")
    else:
        print("Dropdown does NOT support multiple selection")

    # Select multiple options
    multi_dropdown.select_by_visible_text("Volvo")
    multi_dropdown.select_by_visible_text("Saab")

    # Print first selected option
    print("First selected option:", multi_dropdown.first_selected_option.text)

    # Print all selected options
    print("Selected options:")
    for option in multi_dropdown.all_selected_options:
        print(option.text)

    # Deselect all options
    multi_dropdown.deselect_all()

    # Print all available options in the dropdown
    print("All available options:")
    for option in multi_dropdown.options:
        print(option.text)

    # Wait before closing the browser
    time.sleep(3)
