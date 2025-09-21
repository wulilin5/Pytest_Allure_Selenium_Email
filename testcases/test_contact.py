from time import sleep

import allure
import pytest

from actions.loginactions import LoginActions
from tools.read_json import read_json
from paths_manager import login_json, contact_json
from common.driver import DriverOperate
from pages.page_contact import PageContact
from actions.contact_actions import ContactActions

global_var = 0

def get_data_add(path):
    data = read_json(path)
    print(data)
    arrs = []
    for data in data.values():
        arrs.append((data['name'], data['email'], data['success'], data['expect_result']))
    return arrs


@allure.epic("163邮箱网站管理联系人测试")
@allure.feature("管理联系人测试")
class TestContact:
    parameter = get_data_add(contact_json)

    @pytest.mark.parametrize("name, email, success, expect_result", parameter)
    def test_contact_add(self, name, email, success, expect_result):
        allure.dynamic.title(f'{expect_result}')

        global global_var
        if global_var == 0:
            global_var = 1
            LoginActions().Login("wulilin55", "Wu@200255Lilin")

        DriverOperate.globalDriverOperate.switch_to_default()

        ContactActions().Contact(name, email, first_time=(global_var==1))
        if success:
            try:
                success_info = PageContact().page_get_success_info()
                print("success_info: ", success_info)

                # 删除联系人
                ContactActions().DeleteContact(email)
                sleep(2)

                # 验证删除成功
                delete_success_info = PageContact().page_get_delete_success_info()
                print("删除成功提示:", delete_success_info)
                assert delete_success_info == "您已成功删除联系人"

                # assert success_info == expect_result
            except Exception:
                DriverOperate.globalDriverOperate.screenshot()
        else:
            error_info = PageContact().page_get_error_info()
            print("error_info: ", error_info)
            try:
                assert error_info == expect_result
            except Exception:
                DriverOperate.globalDriverOperate.screenshot()
                pytest.assume(expect_result == error_info)
        sleep(2)
