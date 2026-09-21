# Eureka_Website_Automation_Testing_Case_2

## Overview

This repository contains the **Case_2 automation script**. It is developed using **Python and Selenium** to automate **Access_Typed_Controlled book and book chapter search and download actions** on the Eureka Website. The script is developed and executed using **PyCharm IDE**.

## Test Case Summary

This positive test case verifies that a user can successfully search for and download assigned **Access_Typed_Controlled books or Access_Typed_Controlled book chapters** from the Eureka Website.

The user logs in with valid credentials and searches for the required book or book chapter by entering its title or keyword in the Search field. After clicking the Search button, the system displays the relevant book or chapter.

If the selected content is assigned to the user by the administrator, the user can download the permitted content. The test case verifies both **chapter-level downloads and complete-book downloads**.

The test case also verifies a chapter download using the **right-click functionality**, where the chapter link is opened in a new tab/window and the user downloads the chapter from the newly opened page.

## Steps in Brief

* The user logs in with valid Eureka credentials.
* The user enters the required book or chapter name/keyword in the Search field.
* The user clicks the Search button.
* The system displays the relevant book or chapter.
* The user downloads the selected chapter or complete book.
* A different chapter of Book 1 is searched and downloaded.
* Complete Book 2 is searched and downloaded.
* A chapter of Book 3 is searched and opened using the right-click option.
* The chapter opens in a new tab/window.
* The user downloads the chapter from the newly opened page.
* The system verifies that the selected authorized content is downloaded successfully.

---

## Books Overview for Test Case

### First Book – Chapter Download

**Book:** 2-Deoxy-D-Glucose: Chemistry and Biology

**Action:**

* Search and download Chapter #1.
* Search and download a different chapter of the same book.

### Second Book – Complete Book Download

**Book:** 2D Materials: Chemistry and Applications (Part 1)

**Action:**

* Search for the book title/keyword.
* Display Book 2 details.
* Download the complete book PDF.

### Third Book – Chapter Download Using Right-Click

**Book:** 2D Materials: Chemistry and Applications (Part 2)

**Action:**

* Search for a chapter of Book 3.
* Display the searched chapter.
* Right-click the chapter link.
* Open the chapter link in a new tab/window.
* Download the chapter from the newly opened page.

---

## Test Case Details

The detailed test case contains the following information:

* Test Case Description
* Test Case ID
* Priority
* Test Designed Date
* Test Execution Date
* Testing Type
* Designed By
* Reviewed By
* Test Type
* Result
* Test Case Type
* Pre-conditions
* Steps of Execution
* Post-conditions
* Expected Output

**Test Case ID:** Case# 2

**Priority:** HIGH

**Test Type:** FUNCTIONAL

**Test Case Type:** POSITIVE

**Testing:** AUTOMATION

**Designed By:** NIDA MAQBOOL

**Result:** PASS

The test case was designed on **12-Jan-2026**.

---

## Preconditions

Before executing the test case:

1. User must be registered by the administrator.
2. User must have valid login credentials.
3. User must have access to the assigned books.
4. User must be able to log in successfully to the Eureka Website.

The test case specifically requires assigned book access before the search and download operations are performed.

---

## Login Flow

The automation performs the following login actions:

1. User clicks on the **Login** option from the Navigation Bar.
2. User enters a valid **Username and Password**.
3. User enters the **Captcha** correctly.
4. User clicks on the **Login** button.
5. User is successfully redirected to the **Home page**.

After successful authentication, the automation continues with the Access_Typed_Controlled book and chapter search/download flow.

---

# Access_Typed_Controlled – Search & Download

## 1. Search & Download Chapter #1 of Book 1

**Book:** 2-Deoxy-D-Glucose: Chemistry and Biology

The automation performs the following actions:

1. User navigates to the Home page.
2. User enters the name of a chapter from Book 1 in the Search field.
3. User clicks the Search button.
4. System displays the searched Chapter #1.
5. User clicks the Download button.

The expected behavior is that the searched chapter is displayed correctly and the selected chapter is downloaded successfully.

---

## 2. Search & Download a Different Chapter of Book 1

**Book:** 2-Deoxy-D-Glucose: Chemistry and Biology

The automation then searches for another chapter from the same book.

Steps:

1. User enters a different chapter name of Book 1 in the Search field.
2. User clicks the Search button.
3. System displays the relevant Chapter #2.
4. User clicks the Download button.

The test verifies that the correct chapter search result is displayed and that the selected chapter is downloaded successfully.

---

## 3. Search & Download Complete Book 2

**Book:** 2D Materials: Chemistry and Applications (Part 1)

The automation performs the following actions:

1. User enters the Book 2 title or keyword in the Search field.
2. User clicks the Search button.
3. System displays the details of Book 2.
4. User clicks the Download option.

The expected result is that the complete Book 2 PDF is downloaded successfully.

---

## 4. Search Chapter of Book 3 Using Right-Click & Download

**Book:** 2D Materials: Chemistry and Applications (Part 2)

The automation performs the following actions:

1. User enters a chapter name of Book 3 in the Search field.
2. User clicks the Search button.
3. System displays the searched chapter.
4. User right-clicks the chapter link.
5. The chapter link is redirected/opened in a new tab or window.
6. The new page is displayed.
7. User clicks the Download option.

This verifies that the searched chapter can be opened through the right-click/new-tab flow and downloaded successfully.

---

# Post-Conditions

After successful execution:

1. Chapter #1 of Book 1 is downloaded successfully.
2. A different chapter of Book 1 is downloaded successfully.
3. The complete Book 2 PDF is downloaded successfully.
4. The selected chapter of Book 3 is downloaded successfully.

These post-conditions are based on the Case #2 test case definition.

---

# Expected Output

The expected results of this test case are:

1. The searched chapter is displayed correctly.
2. The selected chapter is downloaded successfully.
3. The correct chapter search result is displayed.
4. The selected chapter is downloaded successfully.
5. Book 2 is downloaded successfully.
6. The selected Book 3 chapter opens in a new page successfully.
7. The chapter is downloaded successfully.

The expected output verifies both the search functionality and the download functionality for authorized books and chapters.

---

# Folder Structure

```text
Eureka_Website_Automation_Testing_Case_2/
│
├── .env
├── Case_2.py
├── Case_2.xlsx
├── requirements.txt
├── Automation_Report.html
└── README.md
```

> The folder/file names above should be adjusted if your actual Case_2 repository uses different filenames.

---

# Test Case Excel

## Case_2.xlsx

The **Case_2.xlsx** file contains the complete test case documentation.

### Contains:

* Test Case Description
* Steps of Execution
* Pr
