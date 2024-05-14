import path_modifier
path_modifier.modify_sys_path()
from behave import given, when, then
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chrome import chrome
from constants import DELAY_TIME,SEE_TIME
import time as thread

driver = chrome() 

@given(u'User should login to swag labs using correct {username} and {password}')
def step_impl(context, username, password):
    driver.get('https://www.saucedemo.com')
    thread.sleep(SEE_TIME)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
    thread.sleep(SEE_TIME)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    thread.sleep(SEE_TIME)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "login-button"))).click()
    thread.sleep(SEE_TIME)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn"))).click()
    thread.sleep(SEE_TIME)
    thread.sleep(3)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "reset_sidebar_link"))).click()
    driver.refresh()
    thread.sleep(SEE_TIME)
    thread.sleep(DELAY_TIME)

@given(u'User opens the {item} page')
def step_impl(context, item):
    if item == "Sauce Labs Backpack":
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "item_4_title_link"))).click()
    elif item == "Sauce Labs Bike Light":
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "item_0_title_link"))).click()
    elif item == "Sauce Labs Bolt T-Shirt":
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "item_1_title_link"))).click()
    elif item == "Sauce Labs Fleece Jacket":
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "item_5_title_link"))).click()
    elif item == "Sauce Labs Onesie":
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "item_2_title_link"))).click()
    elif item == "Test.allTheThings() T-Shirt (Red)":
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "item_3_title_link"))).click()
    thread.sleep(SEE_TIME)

@when(u'User adds {item} to cart')
def step_impl(context, item):
    item_dash = item.replace(" ", "-")
    item_lower_dash = item_dash.lower()
    add_button = None
    add_button_text = ""
    try:
        add_button = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID,"add-to-cart-"+item_lower_dash)))
        if add_button.text == "Add to cart":
            add_button.click()
        add_button = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID,"remove-"+item_lower_dash)))
        add_button_text = add_button.text

    except TimeoutException:
        try:
            add_button = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID,"add-to-cart")))
            if add_button.text == "Add to cart":
                add_button.click()
            add_button = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID,"remove")))
            add_button_text = add_button.text
        except TimeoutException:
            pass
    assert add_button_text == "Remove", "Add to cart button is not working"
    thread.sleep(SEE_TIME)    


@then(u'User should see {item} in from cart')
def step_impl(context, item):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "shopping_cart_container"))).click()
    thread.sleep(SEE_TIME)
    items = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))
    item_is_added = False
    for i in items:
        if i.text == item:
            item_is_added = True
            break
    assert item_is_added, "Item is not added to cart"
    thread.sleep(SEE_TIME)


