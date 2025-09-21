from selenium import webdriver
import pages

class GetDriver:
    # driver是类变量，初始为None，用于存放浏览器驱动对象。
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(pages.url)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 将 driver 变量置为 None，表示浏览器已关闭，下一次 get_driver 会重新创建
            cls.driver = None