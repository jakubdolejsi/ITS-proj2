import time

from behave import *
from selenium.webdriver.common.by import By


@given("web browser is at e-shop register page")
def step_impl(context):
    context.browser.get('http://mys01.fit.vutbr.cz:8014/index.php?route=account/register')


@when("all required fields are filled")
def step_impl(context):
    context.browser.find_element(By.ID, "input-firstname").click()
    context.browser.find_element(By.ID, "input-firstname").send_keys("Aa")
    context.browser.find_element(By.ID, "input-lastname").send_keys("Aa")
    context.browser.find_element(By.ID, "input-email").send_keys("abba@gmail.com")
    context.browser.find_element(By.ID, "input-telephone").send_keys("607717686")
    context.browser.find_element(By.ID, "input-address-1").click()
    context.browser.find_element(By.ID, "input-address-1").send_keys("aaaa")
    context.browser.find_element(By.ID, "input-city").send_keys("Jihlava")
    context.browser.find_element(By.ID, "input-postcode").send_keys("58601")
    context.browser.find_element(By.ID, "input-country").click()
    dropdown = context.browser.find_element(By.ID, "input-country")
    dropdown.find_element(By.XPATH, "//option[. = 'United Arab Emirates']").click()
    context.browser.find_element(By.ID, "input-country").click()
    context.browser.find_element(By.ID, "input-zone").click()
    dropdown = context.browser.find_element(By.ID, "input-zone")
    dropdown.find_element(By.XPATH, "//option[. = 'Switzerland']").click()
    context.browser.find_element(By.ID, "input-zone").click()
    context.browser.find_element(By.ID, "input-password").click()
    context.browser.find_element(By.ID, "input-password").send_keys("12345")
    context.browser.find_element(By.ID, "input-confirm").send_keys("12345")


@step("privacy policy is accepted")
def step_impl(context):
    context.browser.find_element(By.NAME, "agree").click()


@when('user clicks on "Continue" button')
def step_impl(context):
    context.browser.find_element_by_xpath('/html/body/div[2]/div/div/form/div/div/input[2]').click()


@then("user account is created")
def step_impl(context):
    context.browser.get('http://mys01.fit.vutbr.cz:8014/index.php?route=account/success')
    title = context.browser.find_element_by_xpath('/html/body/div[2]/div/div/h1').text
    assert 'Your Account Has Been Created!' in title


@given("web browser is at e-shop login page")
def step_impl(context):
    context.browser.get('http://mys01.fit.vutbr.cz:8014/index.php?route=account/login')


@step("all required fields are filled")
def step_impl(context):
    context.browser.find_element(By.ID, "input-email").click()
    context.browser.find_element(By.ID, "input-email").send_keys("a@gmail.com")
    context.browser.find_element(By.ID, "input-password").click()
    context.browser.find_element(By.ID, "input-password").send_keys("12345")


@when('user clicks on "Login" button')
def step_impl(context):
    context.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/form/input').click()


@then("user is logged in")
def step_impl(context):
    context.browser.get('http://mys01.fit.vutbr.cz:8014/index.php?route=account/account')
    time.sleep(1)
    # print(context.browser.find_element_by_xpath('//*[@id="content"]/h2[1]').text)

    test = context.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div/h2').text

    # account = context.browser.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/ul/li[1]/a').text
    # context.browser.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()
    # context.browser.find_element(By.CSS_SELECTOR, ".dropdown-menu > li:nth-child(1) > a").click()
    # account = context.browser.find_element(By.CSS_SELECTOR, "h2:nth-child(1)").text

    # assert 'My Account' in account
    assert 'New Customer' in test
