import path_modifier
path_modifier.modify_sys_path()
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chrome import chrome
from constants import DELAY_TIME,SEE_TIME
import time as thread

driver = chrome() 

@given(u'User should login to swag labs using correct {Username} and {Password}')
def step_impl(context, Username, Password):
    driver.get('https://www.saucedemo.com')
    thread.sleep(SEE_TIME)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(Username)
    thread.sleep(SEE_TIME)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(Password)
    thread.sleep(SEE_TIME)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "login-button"))).click()
    thread.sleep(SEE_TIME)


@when(u'User clicks sort doropdown')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))).click()
    thread.sleep(SEE_TIME)


@when(u'User selects {SortOption}')
def step_impl(context, SortOption):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.XPATH, f"//option[text()='{SortOption}']"))).click()
    thread.sleep(SEE_TIME)


@then(u'User should see the items sorted by {SortOption}')
def step_impl(context, SortOption):
    items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    sorted_items = [item.text for item in items]
    if SortOption == "Name (A to Z)":
        assert sorted_items == sorted(sorted_items), f"Items are not sorted by {SortOption}"
    elif SortOption == "Name (Z to A)":
        assert sorted_items == sorted(sorted_items, reverse=True), f"Items are not sorted by {SortOption}"
    elif SortOption == "Price (low to high)":
        prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices = [float(price.text[1:]) for price in prices]
        assert prices == sorted(prices), f"Items are not sorted by {SortOption}"
    elif SortOption == "Price (high to low)":
        prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices = [float(price.text[1:]) for price in prices]
        assert prices == sorted(prices, reverse=True), f"Items are not sorted by {SortOption}"
    thread.sleep(SEE_TIME)
