#!__author__ = "yf"
"""
测试用例
"""
import unittest
import ddt
from selenium import webdriver
from time import sleep

from PublishCourseClass.page_object.loginPage import loginPageClass
from PublishCourseClass.page_object.publicCoursePge import PublishCourseClass


@ddt.ddt
class TestPublicCourseCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        login = loginPageClass(self.driver, loginPageClass.url)
        login.open()
        login.test_loginPage("astest-fy", "4321")
        sleep(3)

    @ddt.data(["课程标题", "客户端-冯燕", "课时标题", 100])
    @ddt.unpack
    def testPublicCourse(self, *args):
        print(args)
        publishCourse = PublishCourseClass(self.driver, PublishCourseClass.url)
        publishCourse.open()
        publishCourse.test_publishCourse(args[0], args[1], args[2], args[3])
        sleep(2)
        publishCourse.CloseBrowser()

if __name__ == "__main__":
    unittest.main()