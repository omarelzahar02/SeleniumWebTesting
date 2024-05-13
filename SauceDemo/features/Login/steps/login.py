import sys
sys.path.append('C:\\Users\\Youssef Darwish\\Documents\\GitHub\\SeleniumWebTesting')
from behave import given, when, then
from chrome import chrome
from driver import driver
from constants import SITE_NAME, DELAY_TIME
from my_imports import WebDriverWait, EC, By, thread
from helper_functions import locate_element
import time

password = "secret_sauce"

@given(u'a user "{username}" is on the SauceDemo login page')
def step_impl(context, username):
    driver.get('https://www.saucedemo.com')
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "user-name")))


@when(u'the user logs in with username "{username}" and the predefined password')
def step_impl(context, username):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "login-button"))).click()
    thread.sleep(DELAY_TIME)

@then(u'the login should be successful and the user sees the product page')
def step_impl(context):
    assert "Swag Labs" in driver.title, "Login failed or user not on product page"

@when(u'the user attempts to log in with an incorrect password')
def step_impl(context):
    incorrect_password = "wrong_password"    
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(incorrect_password)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "login-button"))).click()
    thread.sleep(DELAY_TIME)


@then(u'a warning should appear that the password is incorrect')
def step_impl(context):
    assert "Epic sadface: Username and password do not match any user in this service" in WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))).text, "Incorrect password warning not found"

@when(u'the user enters only their username and attempts to log in')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "login-button"))).click()
    thread.sleep(DELAY_TIME)

@then(u'a warning should appear that the password cannot be empty')
def step_impl(context):
    assert "Epic sadface: Password is required" in WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))).text, "Password warning not found"


@when(u'the user enters only their password and attempts to log in')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "login-button"))).click()
    thread.sleep(DELAY_TIME)


@then(u'a warning should appear that the username cannot be empty')
def step_impl(context):
    assert "Epic sadface: Username is required" in WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))).text, "Username warning not found"
