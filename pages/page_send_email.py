# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : page_send_email.py
# @author   : wll
# @Time     : 2025/7/18 下午3:03

import pages
from common.driver import DriverOperate
from pages.basepage import BasePage

class PageSendEmail(BasePage):
    def page_click_index(self):
        # 点击首页
        ele_info = {"name": "首页",
                    "type": pages.index_loc[0],
                    "value": pages.index_loc[1]
                    }
        self.operate.click(ele_info)

    # 点击写信
    def page_click_write_email(self):
        ele_info = {"name": "写信",
                    "type": pages.write_email_loc[0],
                    "value": pages.write_email_loc[1]
                    }
        self.operate.click(ele_info)

    # 输入收件人地址
    def page_input_receiver(self, receiver):
        ele_info = {"name": "收件人",
                    "type": pages.receiver_loc[0],
                    "value": pages.receiver_loc[1]
                    }
        self.operate.send_keys(ele_info, receiver)

    # 输入主题
    def page_input_theme(self, theme):
        ele_info = {"name": "主题",
                    "type": pages.theme_loc[0],
                    "value": pages.theme_loc[1]
                    }
        self.operate.send_keys(ele_info, theme)

    # 进入body frame框架
    def page_enter_body_frame(self):
        ele_info = {"name": "body frame",
                    "type": pages.body_frame[0],
                    "value": pages.body_frame[1]
                    }
        el_frame = self.operate.find_element(ele_info)
        self.operate.switch_to_frame(el_frame)

    # 输入body内容
    def page_input_body(self, body):
        ele_info = {"name": "body",
                    "type": pages.body_loc[0],
                    "value": pages.body_loc[1]
                    }
        self.operate.send_keys(ele_info, body)

    # 点击发送
    def page_click_send(self):
        ele_info = {"name": "发送",
                    "type": pages.send_email_loc[0],
                    "value": pages.send_email_loc[1]
                    }
        self.operate.click(ele_info)

    def switch_frame_to_default(self):
        self.operate.switch_to_default()

    # 获取发送成功的text
    def page_get_send_email_success_text(self):
        ele_info = {"name": "发送成功的text",
                    "type": pages.send_email_success_text_loc[0],
                    "value": pages.send_email_success_text_loc[1]
                    }
        return self.operate.get_text(ele_info)

    # 获取发送失败的text
    def page_get_send_email_failed_text(self):
        if self.operate.base_is_input_empty_div({"name": "收件人输入框为空",
                                                 "type": pages.email_strong[0],
                                                 "value": pages.email_strong[1]}):
            print("这里呢")
            return self.operate.get_tip_text({"name": "收件人输入框为空的text",
                                              "type": pages.send_empty_receiver_tip[0],
                                              "value": pages.send_empty_receiver_tip[1]})
        elif self.operate.base_is_input_empty({"name": "主题输入框为空",
                                               "type": pages.theme_loc[0],
                                               "value": pages.theme_loc[1]}):
            text = self.operate.get_text({"name": "主题为空的text",
                                          "type": pages.empty_theme_tip[0],
                                          "value": pages.empty_theme_tip[1]})
            self.operate.click({"name": "取消",
                                "type": pages.cancel_btn[0],
                                "value": pages.cancel_btn[1]})
            return text




