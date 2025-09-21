from time import sleep

import pages
from pages.basepage import BasePage


class PageLogin(BasePage):
    def switch_to_frame_login(self):
        if not self.operate:
            raise RuntimeError("操作对象未初始化，请检查fixture配置")
        ele_info = {"name": "进入frame框架",
                    "type": pages.login_iframe[0],
                    "value": pages.login_iframe[1]}


        el_frame = self.operate.find_element(ele_info)
        self.operate.switch_to_frame(el_frame)

    def switch_frame_to_default(self):
        self.operate.switch_to_default()

    def page_input_account(self, username):
        ele_info = {"name": "邮箱账号或手机号码",
                    "type": pages.login_input_account[0],
                    "value": pages.login_input_account[1]}
        self.operate.send_keys(ele_info, username)
    def page_input_pwd(self, pwd):
        ele_info = {"name": "输入密码",
                    "type": pages.login_input_password[0],
                    "value": pages.login_input_password[1]}
        self.operate.send_keys(ele_info, pwd)
    def page_click_login(self):
        ele_info = {"name": "登录",
                    "type": pages.login_click_login_button[0],
                    "value": pages.login_click_login_button[1]}
        self.operate.click(ele_info)

    def page_is_login_success(self):
        ele_info = {"name": "判断是否登录成功: 出现首页两个字",
                    "type": pages.index_loc[0],
                    "value": pages.index_loc[1]}
        return self.operate.is_element_exist(ele_info)

    def page_click_logout_1(self):
        ele_info = {"name": "退出登录第一步：点击下拉框",
                    "type": pages.login_logout_before[0],
                    "value": pages.login_logout_before[1]}
        self.operate.click(ele_info)

    def page_click_logout_2(self):
        ele_info = {"name": "退出登录第二步：点击退出登录",
                    "type": pages.login_logout[0],
                    "value": pages.login_logout[1]}
        self.operate.click(ele_info)

    def page_is_logout_success(self):
        ele_info = {"name": "判断是否退出成功:您已成功退出邮箱",
                    "type": pages.if_logout[0],
                    "value": pages.if_logout[1]}
        return self.operate.is_element_exist(ele_info)

    def page_relogin(self):
        ele_info = {"name": "退出之后点击重新登录：到登录界面",
                    "type": pages.relogin_button[0],
                    "value": pages.relogin_button[1]}
        self.operate.click(ele_info)


    def page_get_error_info_before(self):
        if self.operate.base_is_input_empty({"name": "用户名是否为空",
                                             "type": pages.login_input_account[0],
                                             "value": pages.login_input_account[1]}):
            return self.operate.get_text({"name": "错误提示信息：请输入账号",
                                          "type": pages.login_phone_lack[0],
                                          "value": pages.login_phone_lack[1]})
        elif self.operate.base_is_input_empty({"name": "密码是否为空",
                                               "type": pages.login_input_password[0],
                                               "value": pages.login_input_password[1]}):
            return self.operate.get_text({"name": "错误提示信息：请输入密码",
                                          "type": pages.login_pwd_lack[0],
                                          "value": pages.login_pwd_lack[1]})
        else:
            return self.operate.get_text({"name": "错误提示信息：账号或密码错误",
                                          "type": pages.login_passwd_fail[0],
                                          "value": pages.login_passwd_fail[1]})


    def switch_to_pwd_login(self):
        ele_info = {"name": "页面是否出现扫码登录",
                    "type": pages.scan_title[0],
                    "value": pages.scan_title[1]}
        if self.operate.is_element_exist(ele_info):
            title_text = self.operate.get_text(ele_info)
            if "扫码登录" in title_text:
                ele_info = {
                    "name": "点击密码登录",
                    "type": pages.switch_to_pwd_btn[0],
                    "value": pages.switch_to_pwd_btn[1]}
                self.operate.click(ele_info)
                sleep(1)

