from behave import given, when, then
from chrome import chrome
from constants import SITE_NAME, DELAY_TIME
from my_imports import WebDriverWait, EC, By, thread
from helper_functions import locate_element
import time
firstName = None
lastName = None
email = None
password = None
driver = chrome()

@given(u'new user want to use the contact list app')
def step_impl(context):
    global firstName, lastName, email, password
    firstName = "Omar"
    lastName = "Elzahar"
    email = "Omar" + str(int(time.time())) + "@gmail.com"
    password = "123456789"


@when(u'the user tries to sign up with first name, last name, email and password')
def step_impl(context):
    driver.get('https://thinking-tester-contact-list.herokuapp.com/addUser')
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(firstName)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "lastName"))).send_keys(lastName)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "submit"))).click()
    thread.sleep(DELAY_TIME)


@then(u'the sign up should be successful')
def step_impl(context):
    assert driver.title == "My Contacts", "Sign up failed"


@given(u'a user exists with username')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a user exists with username')


@then(u'the sign up should be unsuccessful')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the sign up should be unsuccessful')