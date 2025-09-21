# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : driver.py
# @author   : wll
# @Time     : 2024/7/17 下午3:07
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.wait import WebDriverWait

from common.logger import GetLogger
from paths_manager import screenshot_path


def click_success(locator):
    def _predicate(driver):
        try:
            element = driver.find_element(*locator)
            element.click()
            return True
        except:
            print('点击报错了')
            return False

    return _predicate

class DriverOperate:
    # 利用类属性定义一个全局的核心操作对象，他的赋值未来必须在conftest中完成
    globalDriverOperate = None

    def __init__(self, browser='chrome'):
        self.logger = GetLogger.get_logger()
        self.browser = browser.lower()

        if self.browser == 'chrome':
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(options=options)
        elif self.browser == 'firefox':
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(options=options)
        elif self.browser == 'edge':
            options = webdriver.EdgeOptions()
            self.driver = webdriver.Edge(options=options)
        elif self.browser == 'ie':
            options = webdriver.IeOptions()
            self.driver = webdriver.Ie(options=options)
        elif self.browser == 'safari':
            options = webdriver.safari.options.Options()
            self.driver = webdriver.Safari(options=options)
        else:
            self.logger.error(f'{self.browser} 浏览器不支持')
            raise BaseException(f'{self.browser} 浏览器不支持')

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.action = ActionChains(self.driver)
        self.logger.info(f'{self.browser} 启动成功')

    def get(self, url):
        self.driver.get(url)
        self.logger.info(f'{url} 打开成功')

    # 通过不同的type来定位
    def get_locator(self, ele_info):
        l_type = ele_info['type']
        value = ele_info['value']
        if l_type == 'id':
            locator = (By.ID, value)
        elif l_type == 'name':
            locator = (By.NAME, value)
        elif l_type == 'classname':
            locator = (By.CLASS_NAME, value)
        elif l_type == 'tagname':
            locator = (By.TAG_NAME, value)
        elif l_type == 'linktext':
            locator = (By.LINK_TEXT, value)
        elif l_type == 'partiallinktext':
            locator = (By.PARTIAL_LINK_TEXT, value)
        elif l_type == 'css selector':
            locator = (By.CSS_SELECTOR, value)
        elif l_type == 'xpath':
            locator = (By.XPATH, value)
        else:
            self.logger.error(f'定位类型{l_type} 不支持')
            raise BaseException(f'定位类型{l_type} 不支持')
        return locator

    def find_element(self, ele_info):
        # ele_info = {"name":"登录","type":"linktext","value":"登录","timeout":5}
        # timeout可以不写，默认5秒超时
        name = ele_info['name']
        l_type = ele_info['type']
        value = ele_info['value']
        timeout = ele_info.get('timeout', 5)
        locator = self.get_locator(ele_info)
        # 使用显式等待来完成元素定位
        try:
            wait = WebDriverWait(driver=self.driver, timeout=timeout)
            element = wait.until(expected_conditions.presence_of_element_located(locator))
            self.logger.info(f'定位元素【{name}】,通过【{l_type}】,值是【{value}】,定位成功')
            return element
        except BaseException as e:
            self.logger.exception(f'定位元素【{name}】,通过【{l_type}】,值是【{value}】,定位失败')
            raise BaseException(f'定位元素【{name}】,通过【{l_type}】,值是【{value}】,定位失败:{e}')

    def find_elements(self, ele_info):
        # ele_info = {"name":"登录链接","type":"linktext","value":"登录","timeout":5}
        # ele_info的数据格式是我们自行设计的，代表某个元素的基本信息,timeout可以不写，默认5秒超时
        name = ele_info['name']
        type = ele_info['type']
        value = ele_info['value']
        timeout = ele_info.get('timeout', 30)
        locator = self.get_locator(ele_info)
        # 使用显式等待来完成元素定位
        try:
            wait = WebDriverWait(driver=self.driver, timeout=timeout)
            element_list = wait.until(expected_conditions.presence_of_all_elements_located(locator))
            self.logger.info(f'定位元素【{name}】,通过【{type}】,值是【{value}】,定位成功{len(element_list)}个')
            return element_list
        except BaseException as e:
            self.logger.exception(f'定位元素【{name}】,通过【{type}】,值是【{value}】,定位失败')
            raise BaseException(f'定位元素【{name}】,通过【{type}】,值是【{value}】,定位失败:{e}')

    def click(self, ele_info):
        name = ele_info['name']
        type = ele_info['type']
        value = ele_info['value']
        timeout = ele_info.get('timeout', 5)
        locator = self.get_locator(ele_info)
        try:
            wait = WebDriverWait(driver=self.driver, timeout=timeout)
            wait.until(click_success(locator))
            self.logger.info(f'点击元素【{name}】,通过【{type}】,值是【{value}】,点击成功')
        except BaseException as e:
            self.logger.exception(f'点击元素【{name}】,通过【{type}】,值是【{value}】,点击失败')
            raise BaseException(f'点击元素【{name}】,通过【{type}】,值是【{value}】,点击失败:{e}')

    def send_keys(self, ele_info, text, is_clear=True):
        name = ele_info['name']
        type = ele_info['type']
        value = ele_info['value']
        timeout = ele_info.get('timeout', 5)
        element = self.find_element(ele_info)
        try:
            if is_clear:
                element.clear()
                self.logger.info(f'清除元素【{name}】内容成功')
            element.send_keys(text)
            self.logger.info(f'向元素【{name}】,通过【{type}】,值是【{value}】,输入【{text}】成功')
        except BaseException as e:
            self.logger.exception(f'向元素【{name}】,通过【{type}】,值是【{value}】,输入【{text}】失败')
            raise BaseException(f'向元素【{name}】,通过【{type}】,值是【{value}】,输入【{text}】失败:{e}')

    def switch_to_frame(self, frame):
        try:
            self.driver.switch_to.frame(frame)
            self.logger.info(f'切换到iframe:【{frame}】成功')
        except BaseException as e:
            self.logger.exception(f'切换到iframe:【{frame}】失败')
            raise BaseException(f'切换到iframe:【{frame}】失败:{e}')

    def switch_to_default(self):
        self.driver.switch_to.default_content()
        self.logger.info(f'切换到默认页面成功')

    def page_contains(self, text, timeout=5):
        try:
            wait = WebDriverWait(driver=self.driver, timeout=timeout)
            wait.until(lambda d: text in d.page_source)
            self.logger.info(f'判断页面包含【{text}】成功')
            return True
        except BaseException as e:
            self.logger.exception(f'判断页面包含【{text}】失败')
            return False

    def is_element_exist(self, ele_info):
        try:
            self.find_element(ele_info)
            return True
        except:
            return False



    # 典型使用场景示例：
    # 激活下拉菜单
    # 显示工具提示
    # 处理需要悬停才能点击的按钮
    # 触发AJAX加载的内容
    def move_to_element(self, ele_info):
        name = ele_info['name']
        type = ele_info['type']
        value = ele_info['value']
        timeout = ele_info.get('timeout', 5)
        element = self.find_element(ele_info)
        action = ActionChains(self.driver)
        try:
            action.move_to_element(element).perform()
            self.logger.info(f'光标移动到元素【{name}】,通过【{type}】,值是【{value}】,成功')
        except BaseException as e:
            self.logger.exception(f'光标移动到元素【{name}】,通过【{type}】,值是【{value}】,失败')
            raise BaseException(f'光标移动到元素【{name}】,通过【{type}】,值是【{value}】,失败:{e}')


    def get_text(self, ele_info):
        text = self.find_element(ele_info).text

        print("text:", text)

        self.logger.info(f'获取元素【{ele_info["name"]}】的文字是:{text}')
        return text


    """
    获取提示文本（针对提示信息弹窗或隐藏元素）
    
    原因：
    --------
    - 前端提示信息可能使用动态渲染（如 innerText 通过 JS 填充）
    - 或提示框被隐藏（display:none），导致 Selenium 的 element.text 获取不到值
    - 普通 get_text 方法在这种情况下会返回空字符串，无法断言提示内容

    处理逻辑：
    --------
    1. 先等待提示文本非空：
       - 检查 element.text、innerText、textContent 三种可能来源
       - 保证提示信息已经渲染到 DOM
    2. 三层兜底获取文本：
       - 优先取 element.text（可见文本）
       - 取不到则用 element.get_attribute("innerText")
       - 仍取不到则强制执行 JS，获取隐藏元素 innerText
       
    3、为什么不是 get_text: get_text 适合可见文本;提示框 often 被隐藏（display:none），Selenium 拿不到
    4、为什么要三层兜底： .text → 只能拿可见；innerText → 可拿隐藏文本；JS 强制获取 → 保底（绕过所有限制）
    5、为什么要等待：前端渲染提示信息有延迟，必须等到填充后再取
    """
    def get_tip_text(self, ele_info):
        element = self.find_element(ele_info)
        wait = WebDriverWait(driver=self.driver, timeout=ele_info.get('timeout', 5))
        wait.until(lambda driver: (
                element.text.strip() != "" or
                element.get_attribute("innerText").strip() != "" or
                element.get_attribute("textContent").strip() != ""
        ))

        # 三层兜底
        text = (
                element.text.strip() or
                element.get_attribute("innerText").strip() or
                self.driver.execute_script("return arguments[0].innerText;", element).strip()
        )
        self.logger.info(f'获取提示文本【{ele_info["name"]}】: {text}')
        return text

    '''可以获取任意属性值 包含日志记录功能 需要显式指定属性名参数'''
    def get_attribute(self, ele_info, attr_name):
        element = self.find_element(ele_info)
        value = element.get_attribute(attr_name)
        self.logger.info(f'获取元素【{ele_info["name"]}】的属性【{attr_name}】是:{value}')
        return value

    def is_input(self, ele_info):
        input_text = self.get_text(ele_info)
        return len(input_text.strip()) == 0


    def get_screenshot_as_file(self, filename):
        try:
            self.driver.get_screenshot_as_file(filename)
            self.logger.info(f'截图成功,保存文件【{filename}】')
        except BaseException as e:
            self.logger.exception(f'截图失败')
            raise BaseException(f'截图失败')

    def get_screenshot_as_png(self):
        return self.driver.get_screenshot_as_png()

    def base_move_to_empty_space(self):
        self.action.move_by_offset(0, 0)
        self.action.click()
        self.action.perform()
        time.sleep(1)

    def quit(self):
        self.driver.quit()

    def refresh(self):
        self.driver.refresh()

    def screenshot(self):
        self.driver.get_screenshot_as_file("{}/{}.png".format(screenshot_path, time.strftime("%Y_%m_%d_%H_%M_%S")))


    def base_is_input_empty(self, ele_info):
        input_text = self.get_attribute(ele_info, "value")
        # 去除空格后判断是否长度为0
        # .strip() 去除前后空格，避免 " " 被误判为“有内容”
        return len(input_text.strip()) == 0
    def base_get_value_div(self, ele_info, attr="value"):
        try:
            elem = self.find_element(ele_info)
            if elem:
                value = elem.get_attribute(attr)
                self.logger.info(f'获取元素【{ele_info["name"]}】属性【{attr}】: {value}')
                return value
            else:
                return None

        except BaseException as e:
            self.logger.exception(f'获取元素【{ele_info["name"]}】属性【{attr}】失败')
            self.screenshot()
            raise BaseException(f'获取元素【{ele_info["name"]}】属性【{attr}】失败: {e}')


    """重点地方  div判断元素是否为空"""
    def base_is_input_empty_div(self, ele_info):
        try:
            """因为网易邮箱的用户名那里输入完之后就是一个div，他get_attribute的addr应该是title不是value
            所以这里判断是否empty要专门为div建立一个，而不是用base_is_input_empty"""
            # 先判断元素是否存在，
            if not self.is_element_exist(ele_info):
                self.logger.info(f'元素【{ele_info["name"]}】未生成，视为空')
                return True
            # 2. 获取元素的title属性值（网易邮箱特殊场景）
            # input_text = self.base_get_value_div(ele_info, attr="title")
            # 这里get_value也可以用这个，只是传参的问题，最后都是调用自带的element.get_attribute
            input_text = self.get_attribute(ele_info, attr_name="title")

            # print("inputtext:", input_text)
            # 这里判断是否为空是因为要是为空就不能.strip()
            # 3. 处理None值情况
            if input_text is None:
                self.logger.info(f'元素【{ele_info["name"]}】的属性【title】为 None，视为空')
                return True
            # 4. 判断实际内容是否为空（去除前后空格）
            is_empty = len(input_text.strip()) == 0
            # print("is_empty:", is_empty)
            self.logger.info(f'判断元素【{ele_info["name"]}】是否为空: {is_empty}')
            return is_empty
        except BaseException as e:
            # 异常处理：记录日志、截图并抛出异常
            self.logger.exception(f'判断元素【{ele_info["name"]}】是否为空失败')
            self.screenshot()
            raise BaseException(f'判断元素【{ele_info["name"]}】是否为空失败: {e}')

