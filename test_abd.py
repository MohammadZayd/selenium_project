import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from allure_commons.types import AttachmentType

def setup_function():
    global driver
    options = Options()
    options.add_argument('--headless')
    #hub_url = "http://192.168.100.53:4444/wd/hub"   #windows
    #hub_url = "http://192.168.100.14:4444/wd/hub"
    #driver= webdriver.Remote(command_executor=hub_url,options=options)
    driver = webdriver.Chrome(options=options)
    driver.get("https://alnafi.com/auth/sign-in")
    driver.minimize_window()

def teardown_function():
    driver.quit()
def my_cred():
    return [
        ('testuser','test123'),
        ('hello','shello'),
        ('myname','mypass')
    ]

@pytest.mark.parametrize('username,password',my_cred())
def test_login(username,password):
    print("My pytest login")
    driver.find_element(By.NAME,'email').send_keys(username)
    time.sleep(0.7)
    driver.find_element(By.NAME,'password').send_keys(password)
    #allure.attach(driver.get_screenshot_as_png(),name="myalnafi_sc",attachment_type=AttachmentType.PNG)