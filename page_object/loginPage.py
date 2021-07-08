#!__author__ = "yf"
"""
登录页
"""
from selenium.webdriver.common.by import By
from  selenium import webdriver
from time import sleep

from PublishCourseClass.base_page.basePageClass import BasePageClass


class loginPageClass(BasePageClass):

    url = "https://www.ablesky.com/login.do"

    switch_login = (By.XPATH, '//div[@class="login-switch-wrap"]/div')
    usrname = (By.ID, "J_loginUsername")
    psw = (By.ID, "J_loginPassword")
    login_btn = (By.ID, "J_loginBtn")

    def switch_to_loginPage(self):
        self.click(self.switch_login)

    def inputUsrname(self,  txt):
        self.inputText(self.usrname, txt)

    def inputPsw(self, txt):
        self.inputText(self.psw, txt)

    def clickLogin(self):
        self.click(self.login_btn)

    def test_loginPage(self, usrname, pwd):
        self.switch_to_loginPage()
        self.inputUsrname(usrname)
        self.inputPsw(pwd)
        self.clickLogin()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    login = loginPageClass(driver, loginPageClass.url)
    login.open()
    login.test_loginPage("astest-fy", "4321")
    sleep(3)
    login.CloseBrowser()


