from selenium import webdriver
from testdata.data import *
from pages.loginpage import LoginPage
from pages.homepage import HomePage

driver = webdriver.Chrome(executable_path="C:/Users/SRIHARI/PycharmProjects/Framework_POM/drivers/chromedriver.exe")
driver.get(URL)
driver.implicitly_wait(30)
driver.maximize_window()

lp = LoginPage(driver)
lp.enter_un()
lp.enter_pwd()
lp.click_login()

hp = HomePage(driver)
hp.click_logout()



