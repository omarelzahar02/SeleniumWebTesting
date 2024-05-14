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

@when('I click on the more options button')
def step_when_user_clicks_more_options(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn"))).click()
    thread.sleep(DELAY_TIME)

@then('Logout button should be visible')
def step_then_logout_visible(context):
    logout_button = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "logout_sidebar_link")))
    assert logout_button.is_displayed(), "Logout button is not visible"
    thread.sleep(DELAY_TIME)

@when('I click on the logout button')
def step_when_user_clicks_logout(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "logout_sidebar_link"))).click()
    thread.sleep(DELAY_TIME)

@then('I should be logged out')
def step_then_user_logged_out(context):
    assert 'https://www.saucedemo.com/' == driver.current_url, "User is logged out"