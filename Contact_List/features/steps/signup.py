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

@given(u'the user is on the sign up page')
def step_impl(context):
    driver.get('https://thinking-tester-contact-list.herokuapp.com')
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "signup"))).click()


@when(u'the user tries to sign up with first name, last name, email and password')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(firstName)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "lastName"))).send_keys(lastName)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "submit"))).click()
    thread.sleep(DELAY_TIME)


@then(u'the sign up should be successful')
def step_impl(context):
    assert driver.title == "My Contacts", "Sign up failed"


@given(u'a user tries to sign up again with {credential}')
def step_impl(context, credential):
    print(credential)
    if credential == "the same email":
        driver.back()
    
@when(u'the user enters {credential}')
def step_impl(context, credential):
    if credential == "the same email":
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "submit"))).click()
    elif credential == "a password that is too short":
        global password
        password = 12345
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).clear()
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "submit"))).click()
    
    thread.sleep(DELAY_TIME)

@then(u'a warning appears that {message}')
def step_impl(context, message):
    if message == "the email is already in use":
        assert WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "error"))).text == "Email address is already in use", "Email already exists warning not found"
    elif message == "the password is too short":
        assert WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "error"))).text == f"User validation failed: password: Path `password` (`{password}`) is shorter than the minimum allowed length (7).", "Password too short warning not found"