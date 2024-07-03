import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@then(u'Navigate to search page and check')
def search(context):
    try:
        search = context.driver.find_element(By.XPATH, "//input[@placeholder='Search']").is_displayed()
        assert search is True, "Test passed"
        context.driver.close()
    except:
        context.driver.close()
        assert False, "Test failed"

@when(u'Navigate to Directory')
def Navidir(context):
    context.driver.find_element(By.XPATH, "//span[normalize-space()='Directory']").click()

@then(u'User should land on Directory')
def Directorypage(context):
    try:
        directory = context.driver.find_element(By.XPATH, "//h6[normalize-space()='Directory']").is_displayed()
        assert directory is True, "Test passed"
    except:
        context.driver.close()
        assert False, "Test failed"
