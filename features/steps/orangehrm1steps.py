import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import *


@given(u'Launch chrome browser')
def launchbrowser(context):
    context.driver=webdriver.Chrome()
    context.driver.maximize_window()

@when(u'Open orangehrm page')
def Openhomepage(context):
    context.driver.implicitly_wait(10)
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then(u'Verify logo present on homepage')
def Logoverification(context):
    time.sleep(2)
    Logostatus = context.driver.find_element(By.XPATH,"//img[@alt='company-branding']").is_displayed()
    assert Logostatus is True

@then(u'Close the browser')
def Closebrowser(context):
    context.driver.close()
