from selenium.webdriver.common.by import By

# 以下是服务器域名配置地址
# 测试的地址
url = 'https://mail.163.com/'

# *******************************  登录测试部分  *******************************

scan_title = (By.CSS_SELECTOR, "h2.loginbox-title")  # 标题：扫码登录

switch_to_pwd_btn = (By.ID, "switchAccountLogin")    # 切换到密码登录

# 账号
login_input_account = By.XPATH, "//input[@placeholder='邮箱账号或手机号码']"

# 密码
login_input_password = By.XPATH, "//input[@placeholder='输入密码']"

# 登录按钮
login_click_login_button = By.XPATH, "//a[@id='dologin']"

# # 退出按钮
login_logout_before = By.CSS_SELECTOR, "b.js-component-icon.kJ0.nui-ico.nui-ico-dArr"
login_logout = By.XPATH, "//div[text()='退出登录']"

# 判断是否退出成功
if_logout = By.XPATH, "//h1[contains(text(), '您已成功退出邮箱')]"

relogin_button = By.XPATH, "//a[text()='重新登录']"

# 请输入账号
login_phone_lack = By.XPATH, "//div[text()='请输入账号']"
# 请输入密码
login_pwd_lack = By.XPATH, "//div[text()='请输入密码']"
# 登录失败
login_passwd_fail = By.XPATH, "//div[text()='账号或密码错误']"
# iframe 进入frame
login_iframe = By.XPATH, '//*[@id="loginDiv"]/iframe'

# 首页 判断是否登录成功的标志
index_loc = By.XPATH, '//nav[@id="dvMultiTabWrapper"]/div[1]/ul/li[1]/div[3]'

#################################################################################################################
# *******************************  管理联系人  *******************************

# 点击通讯录
contact_tab = By.XPATH, "//div[text()='通讯录']"

# 新建联系人
new_concat_person = By.XPATH, "//span[text()='新建联系人']"

# 未输入邮箱或者邮箱输入错误的提示信息
invalid_email_error = By.XPATH, "//span[contains(text(),'请正确填写')]"

# 联系人姓名
contact_name = By.XPATH, "//label[text()='姓名']/ancestor::dt/following-sibling::dd//input"

# 输入邮箱账号
input_email = By.XPATH, "//span[text()='电子邮箱']/ancestor::dt/following-sibling::dd//input"

# 点击确定
confirm_btn = By.XPATH, "//span[text()='确 定']"

# 添加成功
add_success = By.XPATH, "//span[text()='您已成功添加联系人']"

# 选中联系人复选框（动态用法，示例：填充email）
contact_checkbox_tpl = "//nobr[@title='{}']/ancestor::tr//span[@role='checkbox']"
delete_btn = By.XPATH, "//span[text()='删 除']"
confirm_delete_btn = By.XPATH, "//span[text()='确 定']"
delete_success = By.XPATH, "//span[text()='您已成功删除联系人']"
# *******************************  发送邮件部分  *******************************

# 点击写信
write_email_loc = By.XPATH, "//li[@role='button' and .//span[text()='写 信']]"

# 收件人
receiver_loc = By.XPATH, '//*[@id="dvContainer"]/div[2]/div[1]/section/header/div[1]/div[1]/div/div[2]/div/input'
# 主题
theme_loc = By.XPATH, '//*[@id="dvContainer"]/div[2]/div[1]/section/header/div[2]/div[1]/div/div/input'
body_frame = By.XPATH, '//*[@class="APP-editor-edtr"]/iframe'
body_loc = By.XPATH, '/html/body'
# 发送
send_email_loc = (By.XPATH, '//footer[@class="jp0"]/div[1]')

# 发送邮件成功的text
send_email_success_text_loc = (By.XPATH, '//div[@id="dvContainer"]/div[2]/div[2]/section/h1')


# 错误信息部分
send_empty_receiver_tip = By.XPATH, "//span[text()='请填写收件人地址后再发送']"

invalid_email_tip_title = By.XPATH, "//div[text()='以下邮箱地址无效，将无法成功收到邮件']"

empty_theme_tip = By.XPATH, "//div[text()='确定真的不需要写主题吗？']"

# 要点的是弹窗里的取消按钮，不是页面底部的那个“取消”。
cancel_btn = By.XPATH, "//div[@class='nui-msgbox-ft-btns']//span[text()='取 消']"

# 获取邮箱账号
email_strong = By.XPATH, "//div[contains(@class, 'nui-editableAddr') and contains(@title, '@')]"








