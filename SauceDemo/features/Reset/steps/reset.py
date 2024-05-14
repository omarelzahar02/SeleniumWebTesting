import path_modifier
path_modifier.modify_sys_path()
from behave import given, when, then
from chrome import chrome
from constants import SITE_NAME, DELAY_TIME
from my_imports import WebDriverWait, EC, By, thread
from helper_functions import locate_element
import time

driver=chrome()

@given('I am logged in')
def step_impl(context):
    driver.get('https://www.saucedemo.com')
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "login-button"))).click()
    thread.sleep(DELAY_TIME)
    assert "Swag Labs" in driver.title, "Login failed or user not on product page"

@given('I add an item to the shopping cart')
def step_when_user_adds_item_to_cart(context):
    # Assuming that items have a button with the class name 'add_to_cart_button'
    add_to_cart_button = driver.find_element(By.XPATH, '//*[contains(@id,"add-to-cart-sauce-labs-")]')    
    add_to_cart_button.click()
    thread.sleep(DELAY_TIME)

@then('A remove button appears on that item')
def step_then_remove_button_appears(context):
    # Assuming that the remove button has an ID that contains 'remove-'
    remove_button = driver.find_elements(By.XPATH, '//*[contains(@id, "remove-")]')
    assert len(remove_button) > 0, "Remove button does not appear on the item"

@when('I click on the more options button')
def step_when_user_clicks_more_options(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn"))).click()
    thread.sleep(DELAY_TIME)

@then('Reset button should be visible')
def step_then_reset_visible(context):
    reset_button = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "reset_sidebar_link")))
    assert reset_button.is_displayed(), "reset button is not visible"
    thread.sleep(DELAY_TIME)

@when('I click on the Reset button')
def step_when_user_clicks_logout(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "reset_sidebar_link"))).click()
    thread.sleep(DELAY_TIME)

    # no button with the content of "Remove" is present on the page
@then('No remove buttons are visible')
def no_remove_buttons(context):
    remove_buttons = driver.find_elements(By.XPATH, '//*[contains(@id, "remove-")]')
    assert len(remove_buttons) == 0, "Remove buttons are visible"
    
@then('No number on shopping cart')
def no_number_on_shopping_cart(context):
    specific_span = driver.find_elements(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a/span')
    assert len(specific_span) == 0, "The specific span exists"
    thread.sleep(DELAY_TIME)

@when('I open the shopping cart')
def step_when_user_opens_shopping_cart(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link"))).click()
    thread.sleep(DELAY_TIME)

@then('I should see no items')
def step_then_no_items_in_cart(context):
    cart_items = driver.find_elements(By.CLASS_NAME, 'cart_quantity')
    assert len(cart_items) == 0, "Items are present in the shopping cart"