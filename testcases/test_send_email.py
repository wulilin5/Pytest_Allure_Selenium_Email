from time import sleep

import allure
import pytest

from actions.loginactions import LoginActions
from tools.read_json import read_json
from paths_manager import login_json, send_email_json
from common.driver import DriverOperate
from pages.page_send_email import PageSendEmail
from actions.send_emailactions import SendEmailActions

global_var = 0

def get_data_send(path):
    data = read_json(path)
    print(data)
    arrs = []
    for data in data.values():
        arrs.append((data['address'], data['theme'], data['body'], data['success'], data['expect_result']))
    return arrs

@allure.epic("163邮箱网站发送邮件测试")
@allure.feature("发送邮件测试")
class TestSend:
    parameter = get_data_send(send_email_json)

    @pytest.mark.parametrize("address, theme, body, success, expect_result", parameter)
    def test_send(self, address, theme, body, success, expect_result):
        allure.dynamic.title(f'{expect_result}')

        global global_var
        if global_var == 0:
            global_var = 1
            LoginActions().Login("wulilin55", "Wu@200255Lilin")
        # PageSendEmail().switch_frame_to_default()
        DriverOperate.globalDriverOperate.switch_to_default()

        SendEmailActions().SendEmail(address, theme, body)

        if success:
            try:
                sleep(2)
                text = PageSendEmail().page_get_send_email_success_text()
                assert text == '邮件发送成功'
            except Exception:
                DriverOperate.globalDriverOperate.screenshot()
        else:
            erro_info = PageSendEmail().page_get_send_email_failed_text()
            print("erro_info: ", erro_info)
            try:
                assert erro_info == expect_result
            except Exception:
                DriverOperate.globalDriverOperate.screenshot()
                pytest.assume(expect_result == erro_info)

        sleep(2)
        PageSendEmail().page_click_index()
        sleep(2)
        DriverOperate.globalDriverOperate.refresh()
        sleep(2)






