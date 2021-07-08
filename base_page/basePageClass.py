#!__author__ = "yf"
"""
base page : 对公共的内容进行封装
1. 定位元素
2. 启动浏览器，访问指定的url
3. 关闭浏览器，释放资源
"""
# from selenium import webdriver


class BasePageClass(object):

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def loactor(self, loc):
        return self.driver.find_element(*loc)

    def inputText(self, loc, txt):
        self.loactor(loc).send_keys(txt)

    def click(self, loc):
        self.loactor(loc).click()

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()



    def CloseBrowser(self):
        self.driver.quit()
