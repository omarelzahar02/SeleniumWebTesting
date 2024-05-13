import path_modifier
path_modifier.modify_sys_path()
from behave import given, when, then
from chrome import chrome
from constants import SITE_NAME, DELAY_TIME
from my_imports import WebDriverWait, EC, By, thread
from helper_functions import locate_element
import time

email = None
password = None
driver = chrome()

@given(u'a registered user wants to access the contact list app')      
def step_impl(context):
    global email, password
    email = "youssef.darwish03@eng-st.cu.edu.eg"
    password = "guc4WLi6j3ngJ!e"

@given(u'the user is on the login page')
def step_impl(context):
    driver.get('https://thinking-tester-contact-list.herokuapp.com')

@when(u'the user logs in with a valid email and password')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "submit"))).click()
    thread.sleep(DELAY_TIME)

@then(u'the login should be successful and the user sees the main contact list')
def step_impl(context):
    assert driver.title == "My Contacts"


@given(u'a registered user is on the login page')
def step_impl(context):
    driver.get('https://thinking-tester-contact-list.herokuapp.com')

@when(u'the user tries to log in with an incorrect password')
def step_impl(context):
    global password
    password = "wrongpassword"    
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "submit"))).click()
    thread.sleep(DELAY_TIME)

@then(u'a warning should appear that the password is incorrect')       
def step_impl(context):
    assert WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "error"))).text == "Incorrect username or password"

@given(u'a user is on the login page')
def step_impl(context):
    driver.get('https://thinking-tester-contact-list.herokuapp.com')


@when(u'the user tries to log in with an email that is not registered')
def step_impl(context):
    global email
    email = "unregistered@example.com"
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "submit"))).click()
    thread.sleep(DELAY_TIME)

@then(u'a warning should appear that the account does not exist')      
def step_impl(context):
    assert WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "error"))).text == "Incorrect username or password"
