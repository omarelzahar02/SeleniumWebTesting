from Contact_List.features.steps.chrome import chrome
# from firefox import firefox
from constants import SITE_NAME, DELAY_TIME
from my_imports import WebDriverWait, EC, By, thread
from helper_functions import locate_element


# Prepare the driver
driver = chrome()
# driver = firefox()

# Navigate to the site
driver.get('https://thinking-tester-contact-list.herokuapp.com/')
print(driver.title)