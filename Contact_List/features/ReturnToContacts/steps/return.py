from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import path_modifier
path_modifier.modify_sys_path()
from behave import given, when, then
from chrome import chrome
from constants import SITE_NAME, DELAY_TIME
from my_imports import WebDriverWait, EC, By, thread
from helper_functions import locate_element

email = "ziad@ziad.com"
password = "ziad123"
driver = chrome()
row = None
table_size = None


@given('I am signed in')
def step_impl(context):
    driver.get('https://thinking-tester-contact-list.herokuapp.com')
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "submit"))).click()
    thread.sleep(DELAY_TIME)

@given('I am on the contact list page')
def step_impl(context):    
    global table_size
    table_size = len(WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'myTable'))).find_elements(By.TAG_NAME, 'tr')) - 1
    # assert that the contact list is not empty
    assert len(WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'myTable'))).find_elements(By.TAG_NAME, 'tr')) - 1 > 0

@when('I click on any contact')
def step_impl(context):
    # Find the table
    table = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'myTable')))
    # Find all rows in the table
    rows = table.find_elements(By.TAG_NAME, 'tr')
    # If there are any rows (contacts), click on the first one
    if len(rows) > 1:
        rows[1].click()
    else:
        assert False, "No contacts found to click on."

@then('the contact details should appear')
def step_impl(context):
    # assert this url https://thinking-tester-contact-list.herokuapp.com/contactDetails
    assert driver.current_url == "https://thinking-tester-contact-list.herokuapp.com/contactDetails"

@then('I should see a return button')
def step_impl(context):
    # Code to verify that the return button is visible...
    WebDriverWait(driver, DELAY_TIME).until(EC.visibility_of_element_located((By.ID, "return")))

@when('I click on the return button')
def step_impl(context):
    # Code to click on the return button...
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "return"))).click()

@then('I should return to the contact list page')
def step_impl(context):
    # assert that the current url is https://thinking-tester-contact-list.herokuapp.com
    thread.sleep(DELAY_TIME)
    assert driver.current_url == "https://thinking-tester-contact-list.herokuapp.com/contactList"
