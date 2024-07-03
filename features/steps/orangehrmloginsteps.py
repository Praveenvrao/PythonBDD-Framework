import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'Launch the Chrome browser')
def Browser_launch(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when(u'Open orangehrm homepage')
def Openhomepage(context):
    context.driver.implicitly_wait(10)
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@when(u'Enter username "{user}" and password "{password}"')
def Entercreds(context,user,password):
    context.driver.implicitly_wait(15)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)

@when(u'Click on login button')
def Loginbutton(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

@then(u'User must login and Dashboard should open')
def Dashboardcheck(context):
    try:
        Dashboardtext = context.driver.find_element(By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Dashboard']").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if Dashboardtext == "Dashboard":
        assert True, "Test Passed"
        context.driver.close()
