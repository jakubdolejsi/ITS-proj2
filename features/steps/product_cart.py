import time

from behave import *  # pylint: disable=no-name-in-module


@given('web browser is at e-shop "MacBook" product page')
def step_impl(context):
    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=product/product&path=18_46&product_id=43')


@given('in "Qty" field is 1')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]').click()
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]').clear()
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]').send_keys("1")


@when('user clicks on the "Add to Cart" button')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/button').click()


@then('"MacBook" is added into the shopping cart with quantity 1')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath('/html/body/header/div/div/div[3]/div/button').click()
    count = context.driver.find_element_by_xpath(
        '/html/body/header/div/div/div[3]/div/ul/li[1]/table/tbody/tr/td[3]').text
    context.driver.find_element_by_xpath(
        '/html/body/header/div/div/div[3]/div/ul/li[1]/table/tbody/tr/td[5]/button').click()

    assert 'x 1' in count


@given('in "Qty" field is 5')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]').click()
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]').clear()
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]').send_keys("5")


@then('"MacBook" is added into the shopping cart with quantity 5')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/header/div/div/div[3]/div/button').click()
    count = context.driver.find_element_by_xpath(
        '/html/body/header/div/div/div[3]/div/ul/li[1]/table/tbody/tr/td[3]').text
    context.driver.find_element_by_xpath(
        '/html/body/header/div/div/div[3]/div/ul/li[1]/table/tbody/tr/td[5]/button').click()

    assert 'x 5' in count


@given("web browser is at e-shop shopping cart page")
def step_impl(context):
    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=checkout/cart')


@step('"MacBook" is in the cart')
def step_impl(context):
    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=product/product&path=18_46&product_id=43')
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]').click()
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]').clear()
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]').send_keys("1")
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/button').click()

    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=checkout/cart')


@when('user clicks on the "Remove" button')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/div[2]/div/div/form/div/table/tbody/tr/td[4]/div/span/button[2]').click()
    time.sleep(1)


@then('"MacBook" is removed from the shopping cart')
def step_impl(context):
    alert = context.driver.find_element_by_xpath('/html/body/div[2]/div/div/p').text

    assert 'Your shopping cart is empty!' in alert


@step('"MacBook" is in the cart with quantity "5"')
def step_impl(context):
    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=product/product&path=18_46&product_id=43')
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]').click()
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]').clear()
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]').send_keys("5")
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/button').click()

    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=checkout/cart')


@when('user changes quantity to "1"')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/table/tbody/tr/td[4]/div/input').click()
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/table/tbody/tr/td[4]/div/input').clear()
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/table/tbody/tr/td[4]/div/input').send_keys(
        '1')


@step('clicks to "Update" button')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/div[2]/div/div/form/div/table/tbody/tr/td[4]/div/span/button[1]').click()


@then('"MacBook" is in the shopping cart with quantity "1"')
def step_impl(context):
    qty = context.driver.find_element_by_xpath(
        '/html/body/div[2]/div/div/form/div/table/tbody/tr/td[4]/div/input').get_attribute('value')

    print(qty)
    assert '1' in qty


@step("user is not logged in")
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/a').click()
    try:
        context.driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/ul/li[5]/a').click()
    except:
        pass


@when('user clicks on the "Checkout" button')
def step_impl(context):
    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=product/product&path=18_46&product_id=43')
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]').click()
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]').clear()
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]').send_keys("1")
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/button').click()

    context.driver.get('http://mys01.fit.vutbr.cz:8014/index.php?route=checkout/cart')
    context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/a').click()


@then('checkout page is opened at step "1"')
def step_impl(context):
    time.sleep(5)
    opened = context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[1]/h4/a').get_attribute(
        'aria-expanded')
    step = context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[1]/h4/a').text

    assert 'Step 1: Checkout Options' in step and 'true' in opened


@then('step "2" is shown')
def step_impl(context):
    time.sleep(5)
    opened = context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[1]/h4/a').get_attribute(
        'aria-expanded')
    step = context.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[1]/h4/a').text

    assert 'Step 2: Billing Details' in step and 'true' in opened
