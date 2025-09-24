import allure
import pytest

from tools.read_json import read_json
from paths_manager import login_json
from common.driver import DriverOperate
from pages.page_login import PageLogin
from actions.loginactions import LoginActions

global_error_info = 0
def get_data_login(path):
    datas = read_json(path)
    print(datas)
    parameter = []
    for data in datas.values():
        parameter.append((data['username'], data['password'], data['success'], data['expect_result']))
    return parameter

    # 测试登录
@allure.epic("163邮箱网站登录测试")
@allure.feature("登录测试")
class TestLogin:
    parameter = get_data_login(login_json)

    @pytest.mark.parametrize("username, password, success, expect_result", parameter)
    def test_login(self, username, password, success, expect_result):
        allure.dynamic.title(f'{expect_result}')
        LoginActions().Login(username, password)
        if success:
            # 登录完成 必须退出frame切回主页面操作首页、退出等内容
            PageLogin().switch_frame_to_default()
            flag = PageLogin().page_is_login_success()
            print("flag", flag)
            if flag:

                # 退出登录，为下一次登录做准备
                PageLogin().page_click_logout_1()
                PageLogin().page_click_logout_2()
                # PageLogin().page_click_login()
                PageLogin().page_relogin()
            else:
                DriverOperate.globalDriverOperate.screenshot()
                pytest.assume(flag)
        else:
            # 获取错误信息
            error_info = PageLogin().page_get_error_info_before()
            print("msg", error_info)
            try:
                # 进行断言，判断预期结果和真实结果是否相同
                # python 断言
                assert error_info == expect_result
                # self.assertEqual(msg, expect_result)
            except AssertionError:
                DriverOperate.globalDriverOperate.screenshot()
                pytest.assume(expect_result == error_info)
                # 刷新，为下一次输入做准备
        DriverOperate.globalDriverOperate.refresh()



