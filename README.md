# Eureka_Website_Automation_Testing_Case_2

## Overview

This repository contains the Case_2 automation script. It is developed using Python and Selenium to automate Case Via Searching (Access_Typed Controlled Books) on the Eureka website. The script was developed in PyCharm IDE.

## Test Case Summary:

This positive test case verifies that a user can successfully access and download assigned Access_Typed_Controlled books or Access_Typed_Controlled book chapters from the Eureka Website. The user logs in with valid credentials and, then search for the Access Book or Book Chapter  enter the title/keyword then clicked on thr search button  If the selected book is assigned by the admin, the user is able to download the permitted content, either specific chapters or the complete book. Then the System displays the relevant chapter or books. and User clicks on the Download button for downloading.


## Folder Structure

<img width="593" height="327" alt="image" src="https://github.com/user-attachments/assets/72a262d5-c372-4012-bbbd-0675cd09b7b6" />

.env File

Purpose:

To securely store login credentials and the base URL.

Install dotenv library:

pip install python-dotenv

Python Code to Load .env File:

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv(".env")

# Variables
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
BASE_URL = os.getenv("BASE_URL")

.env File Content:

LOGIN CREDENTIALS

EMAIL=(Your Email)
PASSWORD=(Your Password)

SITE URL

BASE_URL=https://www.eurekaselect.com/

Creating Executable (.exe) File

Install PyInstaller:

pip install pyinstaller

Command to Create Executable:

pyinstaller --onefile --collect-all selenium Case_2.py
