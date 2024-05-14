import path_modifier
path_modifier.modify_sys_path()
from behave import given, when, then
from chrome import chrome
from constants import SITE_NAME, DELAY_TIME
from my_imports import WebDriverWait, EC, By, thread
from helper_functions import locate_element

email = "darwish@gmail.com"
password = "123456789"
driver = chrome()
row = None
table_size = None
first_name_field = None
last_name_field = None
date_birth_field = None
email_field = None
phone_field = None
street1_field = None
street2_field = None
city_field = None
state_field = None
postal_code_field = None
country_field = None

@given(u'the user is logged in')
def step_impl(context):
    driver.get('https://thinking-tester-contact-list.herokuapp.com')
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "submit"))).click()
    thread.sleep(DELAY_TIME)


@given(u'the user is on the contact list page')
def step_impl(context):
    global table_size
    table_size = len(WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'myTable'))).find_elements(By.TAG_NAME, 'tr')) - 1
    print(table_size)
    assert driver.title == "My Contacts", "Log in failed"


@when(u'the user clicks on the row for the contact with first name {first} and last name {last}')
def step_impl(context, first, last):
    name = first + " " + last
    table = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'myTable')))
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cells = row.text.split()
        if cells and name in row.text:
            row.click()
            break
    thread.sleep(DELAY_TIME)

@then(u'the user is navigated to the contact details page')
def step_impl(context):
    global first_name_field, last_name_field, date_birth_field, email_field, phone_field, street1_field, street2_field, city_field, state_field, postal_code_field, country_field
    
    assert WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/header/h1'))).text == "Contact Details", "Navigation failed to Contact Details Page dcssdvsv"

    first_name_field = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'firstName'))).text
    last_name_field = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'lastName'))).text
    date_birth_field = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'birthdate'))).text
    email_field = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'email'))).text
    phone_field = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'phone'))).text
    street1_field = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'street1'))).text
    street2_field = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'street2'))).text
    city_field = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'city'))).text
    state_field = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'stateProvince'))).text
    postal_code_field = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'postalCode'))).text
    country_field = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'country'))).text

@when(u'the user clicks the edit button')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "edit-contact"))).click()

@then(u'the user is navigated to the edit contact page with the contact\'s details filled in')
def step_impl(context):
    assert WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/header/h1'))).text == "Edit Contact", "Navigation failed to Edit Contact Page"

@then(u'the user updates the following details')
def step_impl(context):
    global row
    row = context.table[0]
    thread.sleep(DELAY_TIME)

    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "firstName"))).clear()
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(row['first_name'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "lastName"))).clear()
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "lastName"))).send_keys(row['last_name'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "birthdate"))).clear()
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "birthdate"))).send_keys(row['DOB'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "email"))).clear()
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(row['email'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "phone"))).clear()
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "phone"))).send_keys(row['phone_number'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "street1"))).clear()
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "street1"))).send_keys(row['address 1'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "street2"))).clear()
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "street2"))).send_keys(row['address 2'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "city"))).clear()
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "city"))).send_keys(row['city'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "stateProvince"))).clear()
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "stateProvince"))).send_keys(row['state'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "postalCode"))).clear()
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "postalCode"))).send_keys(row['postal_code'])
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "country"))).clear()
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "country"))).send_keys(row['country'])


@then(u'the user clicks the submit button')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "submit"))).click()
    thread.sleep(DELAY_TIME)


@then(u'the user is navigated back to the contact details page')
def step_impl(context):
    assert WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/header/h1'))).text == "Contact Details", "Navigation failed to go back to Contact Details Page"


@then(u'the contact should be updated in the contact list')
def step_impl(context):
    assert first_name_field == row['first_name'], f"Expected first name to be {row['first_name']}, but was {first_name_field}"
    assert last_name_field == row['last_name'], f"Expected last name to be {row['last_name']}, but was {last_name_field}"
    assert date_birth_field == row['DOB'], f"Expected date of birth to be {row['DOB']}, but was {date_birth_field}"
    assert email_field == row['email'], f"Expected email to be {row['email']}, but was {email_field}"
    assert phone_field == row['phone_number'], f"Expected phone number to be {row['phone_number']}, but was {phone_field}"
    assert street1_field == row['address 1'], f"Expected address 1 to be {row['address 1']}, but was {street1_field}"
    assert street2_field == row['address 2'], f"Expected address 2 to be {row['address 2']}, but was {street2_field}"
    assert city_field == row['city'], f"Expected city to be {row['city']}, but was {city_field}"
    assert state_field == row['state'], f"Expected state to be {row['state']}, but was {state_field}"
    assert postal_code_field == row['postal_code'], f"Expected postal code to be {row['postal_code']}, but was {postal_code_field}"
    assert country_field == row['country'], f"Expected country to be {row['country']}, but was {country_field}"


@then(u'the user should see the error message {message}')
def step_impl(context, message):
    thread.sleep(DELAY_TIME)
    actual_message = WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "error"))).text
    assert actual_message == message, f"Expected error message to be {message}, but was {actual_message}"

@then(u'the user clicks the cancel button')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "cancel"))).click()
    thread.sleep(DELAY_TIME)


@then(u'the contact should not be updated in the contact details page')
def step_impl(context):
    assert first_name_field == WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'firstName'))).text, f"Expected first name to be {first_name_field}, but was {WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'firstName'))).text}"
    assert last_name_field == WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'lastName'))).text, f"Expected last name to be {last_name_field}, but was {WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'lastName'))).text}"
    assert date_birth_field == WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'birthdate'))).text, f"Expected date of birth to be {date_birth_field}, but was {WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'birthdate'))).text}"
    assert email_field == WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'email'))).text, f"Expected email to be {email_field}, but was {WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'email'))).text}"
    assert phone_field == WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'phone'))).text, f"Expected phone number to be {phone_field}, but was {WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'phone'))).text}"
    assert street1_field == WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'street1'))).text, f"Expected address 1 to be {street1_field}, but was {WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'street1'))).text}"
    assert street2_field == WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'street2'))).text, f"Expected address 2 to be {street2_field}, but was {WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'street2'))).text}"
    assert city_field == WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'city'))).text, f"Expected city to be {city_field}, but was {WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'city'))).text}"
    assert state_field == WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'stateProvince'))).text, f"Expected state to be {state_field}, but was {WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'stateProvince'))).text}"
    assert postal_code_field == WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'postalCode'))).text, f"Expected postal code to be {postal_code_field}, but was {WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'postalCode'))).text}"
    assert country_field == WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'country'))).text, f"Expected country to be {country_field}, but was {WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, 'country'))).text}"


@when(u'the user clicks the delete button')
def step_impl(context):
    WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located((By.ID, "delete"))).click()
    thread.sleep(DELAY_TIME)


@then(u'a confirmation dialog should appear')
def step_impl(context):
    assert WebDriverWait(driver, DELAY_TIME).until(EC.alert_is_present()), "Confirmation dialog did not appear"



@when(u'the user confirms the deletion')
def step_impl(context):
    alert = driver.switch_to.alert
    alert.accept()
    thread.sleep(DELAY_TIME)


@then(u'the user is navigated back to the contacts page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user is navigated back to the contacts page')


@then(u'the contact with first name {first} and last name {last} should not be in the contact list')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the contact with first name Hussein and last name Mostafa should not be in the contact list') 