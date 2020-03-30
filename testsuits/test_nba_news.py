# -*- coding:utf-8 -*-

# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
Created on 2019-12-23
@author: 北京-宏哥   QQ交流群：705269076
Project: 《《一头扎进》系列之Python+Selenium框架设计篇5- 价值好几K的框架，不看别后悔，过时不候
'''
# 3.导入模块
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import NewsHomePage
from pageobjects.news_sport_home import SportsNewsHomePage


class ViewNBANews(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_view_nba_views(self):
        # 初始化百度首页，并点击新闻链接
        baiduhome = HomePage(self.driver)
        baiduhome.click_news()
        # 初始化一个百度新闻主页对象，点击体育
        newshome = NewsHomePage(self.driver)
        newshome.click_sports()
        # 初始化一个体育新闻主页，点击NBA
        sportnewhome = SportsNewsHomePage(self.driver)
        sportnewhome.click_nba_link()
        sportnewhome.get_windows_img()


if __name__ == '__main__':
    unittest.main()
