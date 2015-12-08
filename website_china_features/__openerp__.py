# -*- coding: utf-8 -*-
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    'name': "Website China Features",
    'summary': 'Build Your China Features Website',
    'description': """
打造您的中国特色网站
====================
这是个长期维护的应用，因为中国不断的高速变化发展，未来特色完全不可预测，欢迎各种建议交流

主要相关特色集成
----------------
* Baidu Analytics(百度统计——最大的中文网站分析平台)
* Tencent WeChat(微信，是一个生活方式)
* Tencent QQ(QQ空间-分享生活，留住感动)
* Sina Weibo(微博-随时随地发现新鲜事)
* Chinese Renren(人人网，中国领先的实名制SNS社交网络)
    """,
    'author': "renjie",
    'website': "http://renjie.me",
    'category': 'Website',
    'version': '0.1',
    'depends': ['website'],
    'data': [
        'views/website_templates.xml',
        'views/res_config.xml',
    ],
    'demo': [
        'data/demo.xml',
    ],
    'installable': True,
}