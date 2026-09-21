Eureka_Website_Automation_Testing_Case_2

Overview

This repository contains the Case_2 automation script. It is developed using Python and Selenium to automate Access_Typed_Controlled book and book chapter search and download actions on the Eureka website. The script was developed in PyCharm IDE.

Test Case Summary:

This positive test case verifies that a user can successfully access and download assigned Access_Typed_Controlled books or Access_Typed_Controlled book chapters from the Eureka Website. The user logs in with valid credentials and searches for the required book or book chapter by entering its title or keyword in the Search field. After clicking the Search button, the system displays the relevant book or chapter. If the selected content is assigned by the admin, the user is able to download the permitted content, either specific chapters or the complete book. The test case also verifies a chapter download using the right-click functionality, where the chapter link opens in a new tab/window and the user downloads the chapter from the newly opened page.

Steps in brief:

The user logs in with valid credentials.

The user enters the required book or chapter name/keyword in the Search field.

The user clicks on the Search button.

The system displays the relevant book or chapter.

The user downloads the selected chapter or complete book.

A different chapter of Book 1 is searched and downloaded.

Complete Book 2 is searched and downloaded.

A chapter of Book 3 is searched and opened using the right-click option.

The chapter opens in a new tab/window.

The user downloads the chapter from the newly opened page.

The system verifies that the selected authorized content is downloaded successfully.

Books Overview for Test Case

First Book Download (Chapter #1) (2-Deoxy-D-Glucose: Chemistry and Biology)

Second Book Download (Different Chapter) (2-Deoxy-D-Glucose: Chemistry and Biology)

Third Book Download (Complete Book PDF) (2D Materials: Chemistry and Applications (Part 1))

Fourth Book Download (Single Chapter PDF using Right-Click) (2D Materials: Chemistry and Applications (Part 2))

Folder Structure

Eureka_Website_Automation_Testing_Case_2/
│
├── Case#2/
│   │
│   ├── case_2/
│   │   ├── .env                    # Environment variables file (credentials & URL)
│   │   └── Case_2.exe             # Executable file generated from .py script
│   │
│   ├── build/
│   │   └── Case_2/                 # PyInstaller auto-generated files
│   │
│   ├── Case_2.py                   # Main Python automation script
│   ├── Case_2.spec                 # PyInstaller spec file
│   ├── Case_2.xlsx                 # Excel file containing test case details
│   └── README.md

Test Case Details (Excel)

Case_2.xlsx

Contains:

Test Case Description

Steps of Execution

Pre-conditions

Post-conditions

Expected Output

Example Heading:

1 Preconditions:

User must be registered by the admin, have valid login credentials, have access to assigned books, and be logged in successfully to the Eureka Website.

2 Steps of Execution:

Login → Search Book/Chapter → Select Search Result → Download Chapter/Complete Book → Open Chapter in New Tab where applicable → Download.

3 Expected Output:

The searched book or chapter is displayed correctly and the selected authorized chapter or complete book is downloaded successfully.

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
