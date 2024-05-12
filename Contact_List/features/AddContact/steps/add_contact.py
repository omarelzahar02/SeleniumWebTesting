import sys
sys.path.append('C:\\Users\\Zahar\\OneDrive - Cairo University - Students\\CUFE\\Senior1\\Term2\\Consultation\\SeleniumWebTesting')
from behave import given, when, then
from chrome import chrome
from constants import SITE_NAME, DELAY_TIME
from my_imports import WebDriverWait, EC, By, thread
from helper_functions import locate_element
# from driver import driver

email = "darwish@gmail.com"
password = "123456789"
driver = chrome()
row = None

@given(u'the user is logged in')
def step_impl(context):
    driver.get('https://thinking-tester-contact-list.herokuapp.com')
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "submit"))).click()
    thread.sleep(DELAY_TIME)

@given(u'the user is on the contacts page')
def step_impl(context):
    assert driver.title == "My Contacts", "Log in failed"


@when(u'the user clicks the add a new contact button')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "add-contact"))).click()
    thread.sleep(DELAY_TIME)


# @then(u'the user should see a form to add a new contact')
# def step_impl(context):
#     assert driver.title == "Add Contact", "Log in failed"

@when(u'the user enters the following details to add a new contact')
def step_impl(context):
    global row
    row = context.table[0]
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(row['first_name'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "lastName"))).send_keys(row['last_name'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "birthdate"))).send_keys(row['DOB'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(row['email'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "phone"))).send_keys(row['phone_number'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "street1"))).send_keys(row['address 1'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "street2"))).send_keys(row['address 2'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "city"))).send_keys(row['city'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "stateProvince"))).send_keys(row['state'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "postalCode"))).send_keys(row['postal_code'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "country"))).send_keys(row['country'])

@when(u'the user clicks the submit button')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "submit"))).click()

@then(u'the new contact should be added to the contact list')
def step_impl(context):
    global row
    name = row["first_name"] + ' ' + row["last_name"]
    final_email = row['email']

    table = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'myTable')))

    rows = table.find_elements(By.TAG_NAME, 'tr')

    name_found = False
    email_found = False

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        for cell in cells:
            if name in cell.text:
                name_found = True
            if final_email in cell.text:
                email_found = True

    assert name_found, f"Name '{name}' not found in the table."
    assert email_found, f"Email '{final_email}' not found in the table."


# @then(u'the contact with first name Hussein and last name Mosatafa should appear in the contact list')
# def step_impl(context):
    
#     raise NotImplementedError(u'STEP: Then the contact with first name Hussein and last name Mosatafa should appear in the contact list')


# @then(u'the contact with first name Youssef and last name Hassan should appear in the contact list')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then the contact with first name Youssef and last name Hassan should appear in the contact list')