#!__author__ = "yf"
"""
发布直播课程页面
"""

from PublishCourseClass.base_page.basePageClass import BasePageClass
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import time
from selenium.common.exceptions import NoSuchElementException

from PublishCourseClass.page_object.loginPage import loginPageClass


class PublishCourseClass(BasePageClass):
    # use page object model
    # 获取关联元素
    course_name = (By.ID, "J_inputBox")
    teacher_name = (By.XPATH, "//input[@id='J_lecturerId']")
    teacher_name_list = (By.XPATH, '//div[@id="J_speakerBox"]/ul/li')
    class_title = (By.XPATH, '//div[@id="J_studytime"]//input')
    starttime_hour = (By.CLASS_NAME, 'start-hour')
    starttime_min = (By.CLASS_NAME, 'start-min')
    endtime_hour = (By.CLASS_NAME, 'end-hour')
    endtime_min = (By.CLASS_NAME, 'end-min')
    room_num = (By.XPATH, '//input[@id="J_peopleBox"]')
    course_pic = (By.ID, "J_showDefaultPhoto")
    # div下的子元素下标从1开始
    course_pic_one = (By.XPATH, '//div[@id="J_setDefalutPhoto"]//a[1]')
    service_category_leve1 = (By.XPATH, '//div[@id="service-category"]//ul[1]/li[3]')
    service_category_leve3 = (By.XPATH, '//div[@id="service-category"]//ul[3]/li[1]')
    publish_course_btn = (By.ID, "J_postCourse")

    # 变量直接定义在类里面，没用self修饰的，是类变量
    url = "http://www.ablesky.com/liveCourseRedirect.do?action=toPostLiveCourse&organizationId=2249"
    # 元素操作进行封装
    def input_coursename_text(self, txt):
        self.inputText(self.course_name, txt)



    def select_teacher(self, txt):
        sleep(2)
        self.inputText(self.teacher_name, txt)
        sleep(1)
        self.click(self.teacher_name_list)
        sleep(2)

    def input_class_title(self, txt):
        self.inputText(self.class_title, txt)

    def input_class_time(self,startHour, startMin, endHour, endMin):
        self.loactor(self.starttime_hour).send_keys(startHour)
        self.inputText(self.starttime_min, startMin)
        self.inputText(self.endtime_hour, endHour)
        self.inputText(self.endtime_min, endMin)

    def input_roomNum(self, num):
        self.inputText(self.room_num, num)

    def select_coursePic(self):
        # checkbox 选中
        self.click(self.course_pic)
        self.click(self.course_pic_one)

    def select_serviceCategory(self):
        self.click(self.service_category_leve1)
        self.click(self.service_category_leve3)

    def click_publishCourseBtn(self):
        self.click(self.publish_course_btn)


    def test_publishCourse(self, coursenameTitle, teacherName, classTilte, roomNum):
        self.input_coursename_text(coursenameTitle)
        self.select_teacher(teacherName)
        self.input_class_title(classTilte)

        # 获取当前时间
        localtime = time.localtime(time.time())
        local_hour = localtime.tm_hour
        local_min = localtime.tm_min
        start_hour = local_hour + 1
        self.input_class_time(start_hour,local_min,23,local_min)
        self.input_roomNum(roomNum)
        self.select_coursePic()
        self.select_serviceCategory()
        self.click_publishCourseBtn()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    login = loginPageClass(driver, loginPageClass.url)
    login.open()
    login.test_loginPage("astest-fy", "4321")
    sleep(3)
    publishCourse = PublishCourseClass(driver, PublishCourseClass.url)
    publishCourse.open()
    publishCourse.test_publishCourse("课程标题", "客户端-冯燕", "课时标题", 100)
    sleep(2)
    publishCourse.CloseBrowser()
