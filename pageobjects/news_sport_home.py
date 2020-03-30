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


class SportsNewsHomePage(BasePage):
    # NBA入口
    nba_link = "xpath=>.//*[@id='col_focus']/div[1]/div[2]/div/div[2]/div/ul/li[1]/a"

    def click_nba_link(self):
        self.click(self.nba_link)
        self.sleep(2)
