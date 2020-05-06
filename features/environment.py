from selenium import webdriver
import selenium
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#
# def before_all(context):
#     dp = {'browserName': 'Chrome', 'javascriptEnabled': 'true'}
#     context.driver = webdriver.Remote(command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub',
#                                        desired_capabilities=DesiredCapabilities.CHROME)
#     context.driver.implicitly_wait(15)
#     context.base_url = "http://mys01.fit.vutbr.cz:8014/"
#
#
# def after_all(context):
#     context.driver.quit()

def before_all(context):
    context.driver = webdriver.Chrome('chromedriver')
    context.driver.implicitly_wait(15)
    context.base_url = 'http://mys01.fit.vutbr.cz:8014'

def after_all(context):
    context.driver.quit()