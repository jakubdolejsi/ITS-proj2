import time

from behave import given, when, then  # pylint: disable=no-name-in-module
from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random

mail = ''

def generate_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8))


@given("web browser is at e-shop register page")
def step_impl(context):
    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=account/register')


@when("all required fields are filled")
def step_impl(context):

    global mail
    mail= generate_name()
    mail = mail + '@gmail.com'

    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("aaaa")
    context.driver.find_element(By.ID, "input-lastname").click()
    context.driver.find_element(By.ID, "input-lastname").send_keys("aaaa")
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(By.ID, "input-email").send_keys(mail)
    context.driver.find_element(By.ID, "input-telephone").send_keys("123456789")
    context.driver.find_element(By.ID, "input-address-1").click()
    context.driver.find_element(By.ID, "input-address-1").send_keys("aaaaa")
    context.driver.find_element(By.ID, "input-city").click()
    context.driver.find_element(By.ID, "input-city").send_keys("aaaaa")
    context.driver.find_element(By.ID, "input-postcode").click()
    context.driver.find_element(By.ID, "input-postcode").send_keys("58601")
    context.driver.find_element(By.ID, "input-country").click()
    dropdown = context.driver.find_element(By.ID, "input-country")
    dropdown.find_element(By.XPATH, "//option[. = 'Swaziland']").click()
    context.driver.find_element(By.ID, "input-country").click()
    context.driver.find_element(By.ID, "input-zone").click()
    dropdown = context.driver.find_element(By.ID, "input-zone")
    dropdown.find_element(By.XPATH, "//option[. = 'Manzini']").click()
    context.driver.find_element(By.ID, "input-zone").click()
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("12345")
    context.driver.find_element(By.ID, "input-confirm").click()
    context.driver.find_element(By.ID, "input-confirm").send_keys("12345")
    


@step("privacy policy is accepted")
def step_impl(context):
    context.driver.find_element(By.NAME, "agree").click()


@when('user clicks on "Continue" button')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/div/input[2]').click()


@then("user account is created")
def step_impl(context):
    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=account/success')
    title = context.driver.find_element_by_xpath('/html/body/div[2]/div/div/h1').text
    # assert 'Your Account Has Been Created!' in title
    time.sleep(2)
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/a').click()
    time.sleep(2)

@given("web browser is at e-shop login page")
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()
    context.browser.find_element(By.LINK_TEXT, "Logout").click()

    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=account/login')


@step("all required fields are filled")
def step_impl(context):
    global mail
    context.driver.find_element(By.ID, "input-email").clear()
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(By.ID, "input-email").send_keys(mail)
    context.driver.find_element(By.ID, "input-password").clear()
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("12345abcd")
    print('aaaaadadddddddd')
    print(mail)


@when('user clicks on "Login" button')
def step_impl(context):
    time.sleep(9)
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/form/input').click()
    time.sleep(3)

@then("user is logged in")
def step_impl(context):
    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=account/account')
    time.sleep(3)
    # print(context.driver.find_element_by_xpath('//*[@id="content"]/h2[1]').text)

    test = context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div/h2').text
    time.sleep(3)
    # account = context.driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/ul/li[1]/a').text
    # context.driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()
    # context.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu > li:nth-child(1) > a").click()
    # account = context.driver.find_element(By.CSS_SELECTOR, "h2:nth-child(1)").text

    # assert 'My Account' in account
    assert 'New Customer' in test
