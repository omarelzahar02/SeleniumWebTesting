from behave import given, when, then
from chrome import chrome
from constants import SITE_NAME, DELAY_TIME
from my_imports import WebDriverWait, EC, By, thread
from helper_functions import locate_element
username = None
password = None

@given(u'a user exists with username "user1" and password "pass1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a user exists with username "user1" and password "pass1"')


@when(u'the user tries to login with username "user1" and password "pass1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user tries to login with username "user1" and password "pass1"')


@then(u'the login should be successful')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the login should be successful')


@when(u'the user tries to login with username "user1" and password "wrongpass"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user tries to login with username "user1" and password "wrongpass"')


@then(u'the login should be unsuccessful')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the login should be unsuccessful')