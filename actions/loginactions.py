#!/usr/bin python3
# encoding: utf-8 -*-
# @file     : loginactions.py
# @author   : wll
# @Time     : 2025/7/18 下午3:02


from time import sleep

from common.driver import DriverOperate
from pages.page_login import PageLogin



class LoginActions:
    def Login(self, username, password):
        """执行登录操作
        Args:
            username: 用户名
            password: 密码
        """
        page = PageLogin()  # 创建登录页面对象
        page.switch_to_pwd_login()  # 切换到密码登录方式
        page.switch_to_frame_login()  # 切换到登录iframe框架

        page.page_input_account(username)  # 输入用户名
        page.page_input_pwd(password)  # 输入密码
        page.page_click_login()  # 点击登录按钮
if __name__ == '__main__':
    DriverOperate.globalDriverOperate = DriverOperate(browser='chrome')
    DriverOperate.globalDriverOperate.get('https://mail.163.com/')
    LoginActions().Login("wulilin55", "Wu@200255Lilin")
    sleep(5)
    DriverOperate.globalDriverOperate.quit()


