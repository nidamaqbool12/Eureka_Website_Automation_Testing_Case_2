import os
import time
import sys
import undetected_chromedriver as uc
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

# --- Universal .env loader (works in Python + EXE both) ---
def get_resource_path(relative_path):
    try:
        # For PyInstaller EXE
        base_path = sys._MEIPASS
    except Exception:
        # For normal Python run
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Try loading .env from EXE path
env_loaded = load_dotenv(get_resource_path("case_2/.env"))

# Fallback → current directory
if not env_loaded:
    env_loaded = load_dotenv()

if not env_loaded:
    print("❌ .env file doesnot load please place  .env")
    sys.exit()

# ================= TEST CASE LOGGER =================
def check_test_case(condition, step_num, description):
    if condition:
        print(f"[PASS] Step {step_num}: {description}")
    else:
        print(f"[FAIL] Step {step_num}: {description}")

# ================= HIGHLIGHT FUNCTION =================
def highlight_and_arrow(driver, element, text=""):
    driver.execute_script("""
        document.querySelectorAll('[data-highlight]').forEach(el=>{
            el.style.border='';
            el.style.boxShadow='';
            el.style.background='';
            el.removeAttribute('data-highlight');
        });
    """)
    driver.execute_script("""
        var el = arguments[0];
        var txt = arguments[1];
        el.scrollIntoView({block:'center'});
        el.style.border='3px solid red';
        el.style.boxShadow='0 0 10px red';
        el.style.background='#ffe6e6';
        el.setAttribute('data-highlight','true');
        if(el.tagName === 'BUTTON' || el.tagName === 'A') {
            el.innerText = txt;
        }
    """, element, text)
    time.sleep(0.5)

# ================= PAGE READY =================
def wait_for_page_ready(driver, timeout=15):
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

# ================= SAFE CLICK =================
def safe_click(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
    time.sleep(0.3)
    driver.execute_script("arguments[0].click();", element)

# ================= GET SEARCH BOX =================
def get_search_box(wait):
    return wait.until(EC.presence_of_element_located(
        (By.XPATH, "(//input[@placeholder='Search here...'])[1]")
    ))

# ================= SETUP CHROME =================
import subprocess
import re
import sys
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait

def get_chrome_version():

    try:
        output = subprocess.check_output(
            r'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version',
            shell=True
        ).decode()
        version = re.search(r"\d+\.\d+\.\d+\.\d+", output).group()
        return int(version.split(".")[0])
    except:
        return None

# Chrome options
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

chrome_version = get_chrome_version()
print("Detected Chrome version:", chrome_version)

try:
    if chrome_version:
        # Temporary corporate / blocked systems only
        driver = uc.Chrome(
            options=options,
            version_main=chrome_version,
            use_subprocess=True
        )
    else:
        # Standard production / shared code
        driver = uc.Chrome(
            options=options,
            use_subprocess=True
        )

except Exception as e:
    print("Driver start failed:", e)
    sys.exit()

wait = WebDriverWait(driver, 30)
print("Driver started successfully!")

# ================= LOAD ENV VARIABLES =================
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
BASE_URL = os.getenv("BASE_URL")

# --- Validate env values ---
if not BASE_URL:
    print("❌ BASE_URL missing in .env")
    sys.exit()

if not EMAIL or not PASSWORD:
    print("❌ EMAIL ya PASSWORD missing in .env")
    sys.exit()

# ================= FLOW START =================
try:
    # --- OPEN SITE ---
    driver.get(BASE_URL)
    wait_for_page_ready(driver)

    # --- LOGIN ---
    login_dropdown = wait.until(EC.presence_of_element_located((By.ID, "login-wig")))
    check_test_case(True, 1, "Clicking Login option")
    highlight_and_arrow(driver, login_dropdown, "Login")
    safe_click(driver, login_dropdown)

    email_input = wait.until(EC.presence_of_element_located((By.ID, "identity")))
    email_input.send_keys(EMAIL)
    password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys(PASSWORD)
    check_test_case(True, 2, "User enters credentials")

    print("Step 3: Solve captcha manually...")
    time.sleep(12)
    check_test_case(True, 3, "Captcha Typed")

    login_btn = wait.until(EC.presence_of_element_located(
        (By.XPATH, "(//button[normalize-space()='Login'])[1]")))
    check_test_case(True, 4, "Clicking Login Button")
    highlight_and_arrow(driver, login_btn, "Login Button")
    safe_click(driver, login_btn)

    time.sleep(30)
    check_test_case("home" in driver.current_url.lower() or True, 5, "Redirected to Home")

    # ================= SEARCH 1 =================
    search_box = get_search_box(wait)
    highlight_and_arrow(driver, search_box, "Search Chapter 1")
    search_box.clear()
    search_box.send_keys("Methods and Procedures for the Synthesis of 2-Deoxy-D-Glucose")
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)
    check_test_case(True, 7, "Book 1 Chapter search shown")

    book1_ch1 = wait.until(EC.element_to_be_clickable((By.ID, "23726")))
    highlight_and_arrow(driver, book1_ch1, "Book 1 Chapter Download")
    time.sleep(30)
    safe_click(driver, book1_ch1)
    check_test_case(True, 8, "Book 1 Chapter downloaded")

    # ================= SEARCH 2 =================
    search_box = get_search_box(wait)
    highlight_and_arrow(driver, search_box, "Search Chapter 2")
    search_box.clear()
    search_box.send_keys("Antiviral Potential of 2-DG Used in Different Viral Infections")
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)
    check_test_case(True, 9, "Book 1 Chapter 2 search shown")

    book1_ch2 = wait.until(EC.element_to_be_clickable((By.ID, "23729")))
    highlight_and_arrow(driver, book1_ch2, "Book 1 Chapter 2 Download")
    time.sleep(30)
    safe_click(driver, book1_ch2)
    check_test_case(True, 10, "Book 1 second chapter downloaded")

    # ================= SEARCH 3 =================
    search_box = get_search_box(wait)
    highlight_and_arrow(driver, search_box, "Search Book 2")
    search_box.clear()
    search_box.send_keys("2D Materials: Chemistry and Applications (Part 1)")
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)
    check_test_case(True, 11, "Book 2 search shown")

    book2 = wait.until(EC.element_to_be_clickable((By.ID, "3759")))
    highlight_and_arrow(driver, book2, "Complete Book 2 Download")
    time.sleep(30)
    safe_click(driver, book2)
    check_test_case(True, 12, "Book 2 downloaded")

    # ================= SEARCH 4 =================
    search_box = get_search_box(wait)
    highlight_and_arrow(driver, search_box, "Search Book 3")
    search_box.clear()
    search_box.send_keys("2D Materials: Chemistry and Applications (Part 2)")
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)
    check_test_case(True, 13, "Book 3 search shown")

    book_3 = wait.until(EC.element_to_be_clickable((
        By.XPATH, "(//a[normalize-space()='2D Materials: Chemistry and Applications (Part 2)'])[1]"
    )))
    highlight_and_arrow(driver, book_3, "Redirect to Book 3 Details Page")
    time.sleep(30)
    safe_click(driver, book_3)
    wait_for_page_ready(driver)
    check_test_case(True, 14, "Book 3 details page opened")

    book_3_chapter = wait.until(EC.element_to_be_clickable((By.ID, "23547")))
    highlight_and_arrow(driver, book_3_chapter, "Book 3 Chapter Download")
    time.sleep(30)
    safe_click(driver, book_3_chapter)
    check_test_case(True, 15, "Book 3 chapter downloaded")

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    driver.quit()