# -*- coding:utf-8 -*-

# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
Created on 2019-12-23
@author: 北京-宏哥   QQ交流群：705269076
Project: 《《一头扎进》系列之Python+Selenium框架设计篇5- 价值好几K的框架，不看别后悔，过时不候
'''

# 3.导入模块
from framework.base_page import BasePage


class NewsHomePage(BasePage):
    # 点击体育新闻入口
    sports_link = "xpath=>//*[@id='channle-all']/div/ul/li[7]/a"

    def click_sports(self):
        self.click(self.sports_link)
        self.sleep(2)
