import path_modifier
path_modifier.modify_sys_path()
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chrome import chrome
from constants import SITE_NAME, DELAY_TIME, SEE_TIME
import time as thread


driver = chrome() 

@given('User should login to swag labs using correct "{Username}" and "{Password}"')
def step_impl(context, Username, Password):
    driver.get('https://www.saucedemo.com')
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(Username)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(Password)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "login-button"))).click()
    thread.sleep(SEE_TIME)

@given('User clicks the add to cart buttons')
def step_impl(context):
    items = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    for item in items:
        add_button = item.find_element(By.CLASS_NAME, "btn_inventory")
        add_button.click()
    thread.sleep(SEE_TIME)

@given('User clicks the cart icon')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link"))).click()
    thread.sleep(SEE_TIME)

@when('User clicks the remove buttons')
def step_impl(context):
    remove_buttons = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_button")))
    for button in remove_buttons:
        button.click()
    thread.sleep(SEE_TIME)

@then('User should see the cart without the removed item')
def step_impl(context):
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 0, f"Cart still has items, expected 0 but got {len(cart_items)}"
    thread.sleep(SEE_TIME)

@given('User is logged in with "{username}" and "{password}"')
def step_impl(context, username, password):
    driver.get('https://www.saucedemo.com')
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "login-button"))).click()
    thread.sleep(SEE_TIME)

@given('User adds an item to the cart')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "btn_inventory"))).click()
    thread.sleep(SEE_TIME)

@given('User navigates to the cart')
def step_impl(context):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    thread.sleep(SEE_TIME)

@when('User removes the item from the cart')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_button"))).click()
    thread.sleep(SEE_TIME)

@when('User returns to the item listing page')
def step_impl(context):
    driver.find_element(By.ID, "continue-shopping").click()
    thread.sleep(SEE_TIME)

@then('The item button should show "Add to cart"')
def step_impl(context):
    button_text = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "btn_inventory"))).text
    assert button_text == "Add to cart", f"Button text was '{button_text}', expected 'ADD TO CART'"
    thread.sleep(SEE_TIME)