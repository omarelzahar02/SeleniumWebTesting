import path_modifier
path_modifier.modify_sys_path()
from behave import given, when, then
from chrome import chrome
from constants import SITE_NAME, DELAY_TIME
from my_imports import WebDriverWait, EC, By, thread
from helper_functions import locate_element
import time

email = "youssef.darwish03@eng-st.cu.edu.eg"
password = "guc4WLi6j3ngJ!e"
table_size = None

driver=chrome()

@given('a registered user is already logged in')
def step_impl(context):
    driver.get('https://thinking-tester-contact-list.herokuapp.com')
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "submit"))).click()
    thread.sleep(DELAY_TIME)

@given('the user is on the contact list page')
def step_when_user_sees_list(context):
    assert 'contactList' in driver.current_url

@when('the user clicks the logout button')
def step_when_user_clicks_logout(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "logout"))).click()
    thread.sleep(DELAY_TIME)
    
@then('the user should be logged out and redirected to the login page')
def step_then_user_logged_out(context):
    assert 'https://thinking-tester-contact-list.herokuapp.com/' == driver.current_url
    # add delay

    # context.browser.quit()