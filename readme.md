# 自动化测试项目文档

📌 项目概述
基于 Selenium + pytest + Allure 的 163 邮箱 Web 自动化测试框架，采用：

- PO 设计模式（Page Object）
- 数据驱动测试（JSON 数据管理）
- Allure 可视化报告（含失败自动截图）
- 多进程并发执行（pytest-xdist）

🛠️ 功能特性
| 功能模块 | 覆盖场景 | 状态 |
|----------|----------|------|
| 用户登录 | 成功登录/空密码/空账号/错误凭证 | ✅ |
| 联系人管理 | 新建联系人/删除联系人/验证邮箱格式 | ✅ |
| 邮件发送 | 正常发送/空收件人/无效邮箱/空主题 | ✅ |
| 报告系统 | Allure 可视化报告/日志追踪/多语言支持 | ✅ |

🚀 快速开始
## 前置条件
- Java 环境（Allure 依赖）
  ```bash
  # 检查 Java 版本（需 1.8+）
  java -version
  ```
  安装参考：[JDK 安装指南](https://www.oracle.com/java/technologies/downloads/)

- Allure 命令行工具
  ```bash
  # Windows 配置环境变量示例
  PATH=%PATH%;C:\path\to\allure-2.xx.x\bin
  ```
  配置参考：[Allure 官方文档](https://docs.qameta.io/allure/#_installing_a_commandline)

## 环境安装
```bash
# 克隆项目
git clone <项目仓库地址>
cd Pytest_Allure_Selenium_Email

# 创建虚拟环境（可选）
python -m venv .venv
# 激活虚拟环境（Windows）
.venv\Scripts\activate
# 激活虚拟环境（macOS/Linux）
source .venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 验证环境
pytest --version  # 确保 pytest 正常安装
allure --version  # 确保 allure 命令可执行
```

## 执行测试
```bash
# 运行所有测试用例（生成 Allure 原始数据）
pytest

# 多进程并发执行（加快测试速度）
pytest --dist=each

# 生成并查看 Allure 报告
allure serve allure-results
```

## 查看报告
- 通过命令行直接打开（自动启动本地服务）
  ```bash
  allure serve allure-results
  ```
- 或手动生成静态报告后查看
  ```bash
  allure generate allure-results -o allure-report --clean
  # 打开 allure-report 目录下的 index.html 文件
  ```

📂 项目结构
```
Pytest_Allure_Selenium_Email/
├── common/            # 核心封装（驱动/日志工具）
├── pages/             # 页面对象（PO 模式）
├── tools/             # 工具脚本（数据读取等）
├── testcases/         # 测试用例
├── allure-results/    # Allure 报告原始数据
├── allure-report/     # 生成的 Allure 报告（默认不提交仓库）
├── conftest.py        # 全局夹具（驱动初始化/日志配置）
├── pytest.ini         # pytest 配置（用例路径/报告参数）
└── requirements.txt   # 项目依赖清单
```