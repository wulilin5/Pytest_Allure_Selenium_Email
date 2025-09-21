# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : page_contact.py
# @author   : wll
# @Time     : 2025/7/23 下午7:24

import pages
from common.driver import DriverOperate
from pages.basepage import BasePage

class PageContact(BasePage):
    # 点击通讯录
    def page_click_contact(self):
        ele_info = {"name": "点击通讯录",
                    "type": pages.contact_tab[0],
                    "value": pages.contact_tab[1]
                    }
        self.operate.click(ele_info)

    # 点击新增联系人
    def page_click_add_contact(self):
        ele_info = {"name": "新增联系人",
                    "type": pages.new_concat_person[0],
                    "value": pages.new_concat_person[1]
                    }
        self.operate.click(ele_info)



    # 输入联系人姓名
    def page_input_contact_name(self, name):
        ele_info = {"name": "输入联系人姓名",
                    "type": pages.contact_name[0],
                    "value": pages.contact_name[1]
                    }
        self.operate.send_keys(ele_info, name)

    # 输入联系人邮箱账号
    def page_input_contact_email(self, email):
        ele_info = {"name": "输入联系人手机号",
                    "type": pages.input_email[0],
                    "value": pages.input_email[1]
                    }
        self.operate.send_keys(ele_info, email)

    # 点击确认
    def page_click_confirm(self):
        ele_info = {"name": "点击确认",
                    "type": pages.confirm_btn[0],
                    "value": pages.confirm_btn[1]
                    }
        self.operate.click(ele_info)

    # 添加成功提示
    def page_get_success_info(self):
        ele_info = {"name": "获取成功信息",
                    "type": pages.add_success[0],
                    "value": pages.add_success[1]
                    }
        return self.operate.get_text(ele_info)

    # 未输入邮箱账号提示
    def page_get_error_info(self):
        ele_info = {"name": "获取错误信息",
                    "type": pages.invalid_email_error[0],
                    "value": pages.invalid_email_error[1]
                    }
        return self.operate.get_text(ele_info)

    # 选中联系人复选框（根据邮箱定位行）
    def page_select_contact_checkbox_by_email(self, email):
        ele_info = {"name": "选中联系人复选框",
                    "type": "xpath",
                    "value": pages.contact_checkbox_tpl.format(email)
                    }
        self.operate.click(ele_info)

    # 点击页面顶部的“删除”按钮
    def page_click_delete_button(self):
        ele_info = {"name": "点击删除按钮",
                    "type": pages.delete_btn[0],
                    "value": pages.delete_btn[1]
                    }
        self.operate.click(ele_info)

    # 确认删除联系人
    def page_confirm_delete(self):
        ele_info = {"name": "点击确定",
                    "type": pages.confirm_delete_btn[0],
                    "value": pages.confirm_delete_btn[1]
                    }
        self.operate.click(ele_info)

    def page_get_delete_success_info(self):
        ele_info = {"name": "获取删除成功信息",
                    "type": pages.delete_success[0],
                    "value": pages.delete_success[1]
                    }
        return self.operate.get_text(ele_info)

#

