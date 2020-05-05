from behave import *
from selenium.webdriver.common.by import By


@given('"MacBook" is available')
def step_impl(context):
    pass


@given("web browser is opened at e-shop home page")
def step_impl(context):
    context.browser.get('http://mys01.fit.vutbr.cz:8014/')


@when('user types "MacBook" into "Search" bar')
def step_impl(context):
    context.browser.find_element(By.NAME, "search").click()
    context.browser.find_element(By.NAME, "search").send_keys("TEST")
    context.browser.find_element(By.CSS_SELECTOR, ".btn-default").click()


@then('"Not Found" error is shown')
def step_impl(context):
    h1 = context.browser.find_element(By.CSS_SELECTOR, "h1").text
    assert h1 == 'Not Found'


# ---------------------------------------------------------------
@given("web browser is at home e-shop page")
def step_impl(context):
    context.browser.get('http://mys01.fit.vutbr.cz:8014/')


@step('"MacBook" is in the "Featured" section')
def step_impl(context):
    featured = context.browser.find_element(By.CSS_SELECTOR, ".product-layout:nth-child(1) h4").text
    assert featured == 'MacBook'


@when('user clicks on "MacBook" product')
def step_impl(context):
    context.browser.find_element(By.LINK_TEXT, "MacBook").click()


@then('"MacBook" product page is opened')
def step_impl(context):
    context.browser.get('http://mys01.fit.vutbr.cz:8014/index.php?route=product/product&product_id=43')
    h1 = context.browser.find_element(By.CSS_SELECTOR, "h1").text
    assert h1 == 'MacBook'


# ---------------------------------------------------------------
@given('e-shop has "Mac" and "Laptops & Notebooks" category')
def step_impl(context):
    category = context.browser.find_element_by_xpath('/html/body/div[1]/nav/div[2]/ul/li[2]/a').text

    assert 'Laptops & Notebooks' in category


@step('web browser is at e-shop\'s "Macs" category inside "Laptops & Notebooks"')
def step_impl(context):
    context.browser.get('http://mys01.fit.vutbr.cz:8014/index.php?route=product/category&path=18_46')


@when('user clicks on "MacBook"')
def step_impl(context):
    context.browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[1]/h4/a').click()
