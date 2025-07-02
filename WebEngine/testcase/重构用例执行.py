from WebEngine.core.runner import Runner

# 执行环境数据
env_config = {
    "is_debug": False,
    "browser_type": "chromium",
    "host": "http://192.168.1.23:1009",
    "global_variable": {
        "username": "lesso2024",
        "password": "lesso2024"
    }
}
# 测试套件数据
suite = {
    'id': "编号1",
    'name': "登录功能测试",
    # 测试套件的公共前置操作
    'setup_step': [
        {
            "desc": "打开浏览器",
            "method": "open_browser",
            "params": {
                "browser_type": "chromium"
            }
        },
        {
            "desc": "打开网页",
            "method": "open_url",
            "params": {
                "url": "/#/login"
            }
        },
        {
            "desc": "等待2秒",
            "method": "wait_for_time",
            "params": {
                "timeout": 2000
            }
        },
    ],
    # 用例
    "cases": [
{
            'id': "编号1",
            'name': "登录成功",
            "skip": False,
            "steps": [
                {
                    "desc": "等待1秒",
                    "method": "wait_for_time",
                    "params": {
                        "timeout": 1000
                    }
                },
                {
                    "desc": "输入账号",
                    "method": "fill_value",
                    "params": {
                        'locator': '//input[@placeholder="账号"]',
                        'value': "${{username}}"
                    }
                },
                {
                    "desc": "等待1秒",
                    "method": "wait_for_time",
                    "params": {
                        "timeout": 1000
                    }
                },
                {
                    "desc": "输入租户密码",
                    "method": "fill_value",
                    "params": {
                        'locator': '//input[@placeholder="密码"]',
                        'value': "${{password}}"
                    }
                },
                {
                    "desc": "点击登录",
                    "method": "click_ele",
                    "params": {
                        "locator": "button[type='button']"
                    }
                },
                {
                    "desc": "断言是否跳转登录成功后的页面",
                    "method": "assert_page_url",
                    "params": {
                        "expect_results": "http://192.168.1.23:1009/#/welcome"
                    }
                }
            ]
        }

    ]
}

if __name__ == '__main__':
    runner = Runner(env_config, suite)
    res = runner.run()
    print(res)
