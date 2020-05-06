import time
from selenium.webdriver.common.by import By
import string
import random

def generate_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8))


@given('"MacBook" product is available on e-shop')
def step_impl(context):
    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=product/product&path=18_46&product_id=43')
    availability = context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/ul[1]/li[4]').text

    assert 'Availability: In Stock' in availability

@given('a web browser is at e-shop "MacBook" product page')
def step_impl(context):

    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=product/product&path=18_46&product_id=43')

@given('user is actually logged in')
def step_impl(context):

    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=account/register')

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

    context.driver.find_element(By.NAME, "agree").click()
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/div/input[2]').click()


@when('user clicks on the "Add to Wish List" button')
def step_impl(context):

    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=product/product&path=18_46&product_id=43')
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[1]/button[1]').click()

@then('product is added into his wish list')
def step_impl(context):

    alert = context.driver.find_element_by_class_name('alert-success').text

    assert 'Success: You have added MacBook to your wish list!' in alert


@when('user clicks on the "Compare this Product" button')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[1]/button[2]').click()

@then('product is added into his product comparison')
def step_impl(context):
    alert = context.driver.find_element_by_class_name('alert-success').text

    assert 'Success: You have added MacBook to your product comparison!' in alert