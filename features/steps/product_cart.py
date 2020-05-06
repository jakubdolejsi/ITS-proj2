from behave import given, when, then  # pylint: disable=no-name-in-module
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'web browser is at e-shop "MacBook" product page')
def step_impl(context):
    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=product/product&path=18_46&product_id=43')

@given(u'in "Qty" field is 1')
def step_impl(context):
    value = context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]').get_attribute('value')
    
    assert int(value) == 1

@when(u'user clicks on the "Add to Cart" button')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div/button').click()

@then(u'"MacBook" is added into the shopping cart with quantity 1')
def step_impl(context):
    alert = context.driver.find_element_by_xpath('/html/body/div[2]/div[1]').text

    assert 'Success: You have added MacBook to your shopping cart!' in alert

@given(u'in "Qty" field is 5')
def step_impl(context):
    assert False

@then(u'"MacBook" is added into the shopping cart with quantity 5')
def step_impl(context):
    assert False