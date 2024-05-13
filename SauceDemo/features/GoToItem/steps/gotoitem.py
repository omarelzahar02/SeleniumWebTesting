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
item_info = {}


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


@when(u'user clicks on the {item} link')
def step_impl(context, item):
    items = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    thread.sleep(DELAY_TIME)
    for i in items:
        item_children = i.find_elements(By.XPATH,"./child::*")
        item_image_div = item_children[0].find_elements(By.XPATH,".//*")
        item_image = item_image_div[1].get_attribute("src")
        #print(item_image)
        item_name = item_children[1].find_element(By.CLASS_NAME,"inventory_item_name").text
        #print(item_name)
        item_desc = item_children[1].find_element(By.CLASS_NAME,"inventory_item_desc").text
        #print(item_desc)
        item_price = item_children[1].find_element(By.CLASS_NAME,"inventory_item_price").text
        #print(item_price)
        item_info[item_name] = (item_image,item_name,item_desc,item_price)
    print(item_info["Sauce Labs Backpack"])

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


@then(u'User should see the {item} page')
def step_impl(context, item):
    if item == "Sauce Labs Backpack":
        WebDriverWait(driver, DELAY_TIME).until(EC.url_contains("id=4"))
    elif item == "Sauce Labs Bike Light":
        WebDriverWait(driver, DELAY_TIME).until(EC.url_contains("id=0"))
    elif item == "Sauce Labs Bolt T-Shirt":
        WebDriverWait(driver, DELAY_TIME).until(EC.url_contains("id=1"))
    elif item == "Sauce Labs Fleece Jacket":
        WebDriverWait(driver, DELAY_TIME).until(EC.url_contains("id=5"))
    elif item == "Sauce Labs Onesie":
        WebDriverWait(driver, DELAY_TIME).until(EC.url_contains("id=2"))
    elif item == "Test.allTheThings() T-Shirt (Red)":
        WebDriverWait(driver, DELAY_TIME).until(EC.url_contains("id=3"))
    thread.sleep(SEE_TIME)



@then(u'User should see the {item} info is correct')
def step_impl(context, item):
    new_info = {}
    thread.sleep(1)
    item_content = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_container")))
    item_children = item_content.find_elements(By.XPATH,"./child::*")
    item_image_div = item_children[0].find_elements(By.XPATH,"./child::*")
    item_image = item_image_div[0].get_attribute("src")
    temp_div = item_content.find_elements(By.XPATH,".//*")
    item_name = temp_div[3].text
    item_desc = temp_div[4].text
    item_price = item_content.find_element(By.CLASS_NAME,"inventory_details_price").text
    new_info[item] = (item_image,item_name,item_desc,item_price)
    print(new_info[item])
    print(item_info[item])
    assert item_info[item] == new_info[item] , "Item info is not correct"
