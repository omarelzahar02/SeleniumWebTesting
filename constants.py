''' 
This file contains all the constants used in the project
'''
import os
# from dotenv import load_dotenv
# load_dotenv("../Web_Text_Files/.env")


FIREFOX_DRIVER_PATH = "C:/geckodriver.exe"
FIREFOX_BINARY_PATH = "C:/Program Files/Mozilla Firefox/firefox.exe"
DELAY_TIME = 4
SEE_TIME = 1
SITE_NAME = "http://localhost:5173/" #need to be changed
USERNAME = str(os.getenv("USERNAME"))
EMAIL = str(os.getenv("EMAIL"))
PASSWORD = str(os.getenv("PASSWORD"))

