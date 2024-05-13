import sys
sys.path.append('C:\\Users\\Youssef Darwish\\Documents\\GitHub\\SeleniumWebTesting')
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chrome import chrome
from constants import SITE_NAME, DELAY_TIME
import time
driver = chrome() 
username = "standard_user"
@given('User should login to swag labs using correct "{Username}" and "{Password}"')
def step_impl(context, Username, Password):
    global username
    username = Username
    driver.get('https://www.saucedemo.com')
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(Username)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(Password)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "login-button"))).click()

@given('User clicks the add to cart buttons')
def step_impl(context):
    items = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    for item in items:
        add_button = item.find_element(By.CLASS_NAME, "btn_inventory")
        add_button.click()

@given('User clicks the cart icon')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link"))).click()

@when('User clicks the checkout button')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "checkout"))).click()

@when('User enters checkout information with "{FirstName}", "{LastName}", "{ZipCode}"')
def step_impl(context, FirstName, LastName, ZipCode):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(FirstName)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys(LastName)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "postal-code"))).send_keys(ZipCode)

@when(u'User enters checkout information with "John", "Doe", ""')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("John")
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys("Doe")
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "postal-code"))).send_keys("")
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "continue"))).click()


@then(u'User should see an error message "Error: postal code is required"')
def step_impl(context):
    error = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))).text
    assert "Error: Postal Code is required" in error, "Postal code error not found"

@when('User clicks the continue button')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "continue"))).click()

@then('User should see the checkout overview page')
def step_impl(context):
    title = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "title"))).text
    assert "Checkout: Overview" in title, "User not on checkout overview page"

@when('User clicks the finish button')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "finish"))).click()

@then('User should see the order confirmation with "Thank you for your order!"')
def step_impl(context):
    header = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))).text
    assert "Thank you for your order!" in header, "User not on checkout complete page"

@then('User should see an error message "Error: Last Name is required"')
def step_impl(context):
    error = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))).text
    assert "Error: Last Name is required" in error, "Last Name error not found"

@then(u'User should see the cart icon with wrong number of items clicked')
def step_impl(context):
    cart_count = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))).text
    assert "3" in cart_count, "Cart count is not 6"

@then(u'User clicks the cart icon')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link"))).click()


@then(u'Last Name will be empty')
def step_impl(context):
    last_name = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "last-name"))).text
    assert last_name == "", "Last name is not empty"



@then(u'User clicks the continue button')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "continue"))).click()


@then(u'User will stay on the checkout overview page')
def step_impl(context):
    title = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "title"))).text
    assert "Checkout: Overview" in title, "User not on checkout overview page"