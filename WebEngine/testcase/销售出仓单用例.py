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
        }
    ],
    # 用例
    "cases": [
        {
            'id': "编号1",
            'name': "新建销售出仓单",
            "skip": False,
            "steps": [
                {
                    "desc": "点击销售菜单",
                    "method": "click_ele",
                    "params": {
                        "locator": "div.el-sub-menu__title:has-text('销售')"
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
                    "desc": "点击销售出仓单菜单",
                    "method": "click_ele",
                    "params": {
                        #"locator": "//li[./div/span[text()='销售出仓单']]/div"
                        "locator": "span:has-text('销售出仓单')"
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
                    "desc": "点击新单按钮",
                    "method": "click_ele",
                    "params": {
                        "locator": "button:has-text('新单')"
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
                    "desc": "等待客户下拉框placeholder出现",
                    "method": "wait_for_element",
                    "params": {
                        "locator": "//span[text()='请选择客户']"
                    }
                },
                {
                    "desc": "点击选择客户",
                    "method": "click_ele",
                    "params": {
                        "locator": "//span[text()='请选择客户']"
                    }
                },
                {
                    "desc": "等待2秒",
                    "method": "wait_for_time",
                    "params": {
                        "timeout": 2000
                    }
                },
                {
                  "desc": "点击客户选项",
                  "method": "click_ele",
                  "params": {
                    "locator": "//li[@class='el-select-dropdown__item' and text()='城北工地张老板']"
                  }
                },
                {
                    "desc": "等待2秒",
                    "method": "wait_for_time",
                    "params": {
                        "timeout": 2000
                    }
                },
                {
                    "desc": "添加第一个商品",
                    "method": "click_ele2",
                    "params": {
                        "locator": "table.vxe-table--body tr:nth-child(1) td:nth-child(4)"
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
                    "desc": "选择下拉框第一个商品",
                    "method": "click_ele",
                    "params": {
                        "locator": "div.vxe-select--body > div.vxe-select-option:nth-child(1)"
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
                    "desc": "双击修改商品数量",
                    "method": "click_ele2",
                    "params": {
                        "locator": "table.vxe-table--body tr:nth-child(1) td:nth-child(7)"
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
                    "desc": "填入数量",
                    "method": "fill_value",
                    "params": {
                        #"locator": "table.vxe-table--body tr:nth-child(1) td:nth-child(7)",
                        "locator": "//input[@class='vxe-default-input' and @value='0']",
                        'value': "5"
                    }
                },
                {
                    "desc": "点击表格其他空白处保存",
                    "method": "click_ele",
                    "params": {
                        "locator": "table.vxe-table--body tr:nth-child(1) td:nth-child(8)"
                    }
                },
                {
                    "desc": "添加第二个商品",
                    "method": "click_ele2",
                    "params": {
                        "locator": "table.vxe-table--body tr:nth-child(2) td:nth-child(4)"
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
                    "desc": "选择下拉框第2个商品",
                    "method": "click_ele",
                    "params": {
                        "locator": "div.vxe-select--body > div.vxe-select-option:nth-child(2)"
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
                    "desc": "双击修改商品数量",
                    "method": "click_ele2",
                    "params": {
                        "locator": "table.vxe-table--body tr:nth-child(2) td:nth-child(7)"
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
                    "desc": "填入数量",
                    "method": "fill_value",
                    "params": {
                        "locator": "//input[@class='vxe-default-input' and @value='0']",
                        'value': "6"
                    }
                },
                {
                    "desc": "点击表格其他空白处保存",
                    "method": "click_ele",
                    "params": {
                        "locator": "table.vxe-table--body tr:nth-child(2) td:nth-child(8)"
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
                    "desc": "点击返回列表",
                    "method": "click_ele",
                    "params": {
                        "locator": "span:has-text('返回')"
                    }
                 },
            ]
        },
        {
            'id': "编号2",
            'name': "销售出仓单审核",
            "skip": False,
            "steps": [
                {   "desc   ": "刷新页面",
                    "method": "refresh",
                    "params": {
                    }
                },
                {
                    "desc": "点击第一张单据",
                    "method": "click_ele2",
                    "params": {
                        "locator": "table.vxe-table--body tr:nth-child(1) td:nth-child(2)"
                    }
                },
                {
                    "desc": "等待2秒",
                    "method": "wait_for_time",
                    "params": {
                        "timeout": 2000
                    }
                },
                {
                    "desc": "点击审核",
                    "method": "click_ele",
                    "params": {
                        "locator": "button span:has-text('审核')"
                     }
                 },
                {
                    "desc": "等待2秒",
                    "method": "wait_for_time",
                    "params": {
                        "timeout": 2000
                    }
                },
                {
                    "desc": "点击确定",
                    "method": "click_ele",
                    "params": {
                        "locator": "div.el-message-box span:has-text('确定')"
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
