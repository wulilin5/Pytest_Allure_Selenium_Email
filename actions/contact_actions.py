#!/usr/bin python3
# encoding: utf-8 -*-
# @file     : contact_actions.py
# @author   : wll
# @Time     : 2025/7/23 下午8:43


from time import sleep

from pages.page_contact import PageContact
from common.driver import DriverOperate

class ContactActions:
    def Contact(self, name, email, first_time=True):
        page = PageContact()
        if first_time:
            page.page_click_contact()
        sleep(2)
        page.page_click_add_contact()
        sleep(2)
        page.page_input_contact_name(name)
        sleep(2)
        page.page_input_contact_email(email)
        sleep(2)
        page.page_click_confirm()

    def DeleteContact(self, email):
        page = PageContact()
        # 选中联系人复选框
        page.page_select_contact_checkbox_by_email(email)
        sleep(1)
        # 点击删除按钮
        page.page_click_delete_button()
        sleep(1)
        # 确认删除
        page.page_confirm_delete()
