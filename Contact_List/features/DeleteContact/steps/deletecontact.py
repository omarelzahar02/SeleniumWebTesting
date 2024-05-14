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

# Existing steps...

@given('I am logged in')
def step_impl(context):
    driver.get('https://thinking-tester-contact-list.herokuapp.com')
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "submit"))).click()
    thread.sleep(DELAY_TIME)

@given('Contact list is not empty')
def step_impl(context):
    # add a contact
    global table_size
    table_size = len(WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'myTable'))).find_elements(By.TAG_NAME, 'tr')) - 1
    # assert that the contact list is not empty
    assert len(WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'myTable'))).find_elements(By.TAG_NAME, 'tr')) - 1 > 0

@given('I have a contact with the name "{first_name} {last_name}"')
def step_impl(context, first_name, last_name):
    contact_name = first_name + ' ' + last_name

    table = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'myTable')))

    rows = table.find_elements(By.TAG_NAME, 'tr')

    name_found = False

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        for cell in cells:
            if contact_name in cell.text:
                name_found = True

    # output the name of the contact
    print(f"Contact name: {contact_name}")
    assert name_found, f"Name '{contact_name}' not found in the table."

@when('I click on the contact')
def step_impl(context):
    name = context.active_outline['first'] + ' ' + context.active_outline['last']
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.XPATH, f"//td[text()='{name}']"))).click()


@then(u'Contact details should be displayed page')
def step_impl(context):
    # assert this url https://thinking-tester-contact-list.herokuapp.com/contactDetails
    assert driver.current_url == "https://thinking-tester-contact-list.herokuapp.com/contactDetails"

@when(u'I click on the delete button')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "delete"))).click()


@then(u'Website displays a confirmation prompt')
def step_impl(context):
    try:
        WebDriverWait(driver, DELAY_TIME).until(EC.alert_is_present())
    except TimeoutException:
        assert False, "Confirmation prompt did not appear"


@when(u'I click on the confirm button')
def step_impl(context):
    # WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "confirm"))).click()
    alert = WebDriverWait(driver, DELAY_TIME).until(EC.alert_is_present())
    alert.accept()

@then('I am redirected to the contact list page')
def step_impl(context):
    # assert that the current url is https://thinking-tester-contact-list.herokuapp.com
    thread.sleep(DELAY_TIME)
    assert driver.current_url == "https://thinking-tester-contact-list.herokuapp.com/contactList"

@then('the contact should be deleted')
def step_impl(context):
    # assert that the table size is less than the previous table size
    try:
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'myTable')))
        assert False, "Table 'myTable' should not be present"
    except TimeoutException:
        pass