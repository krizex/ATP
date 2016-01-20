# ATP(Air Ticket Price)

[![Build Status](https://travis-ci.org/krizex/ATP.svg)](https://travis-ci.org/krizex/ATP)
-----

This is a crawler which grab the flight info from one famous website of China which used to order air tickets. 

The default behavior of this tool is grabing the flight info of recent 60 days. It certainly contains the lowest price of the ticket in which day you want to have your travel. Once you have collected enough ticket info, you can use some machine learning method to forecast the best day to buy your ticket which will get the lowest price.

## Usage
### Create database
```
cd db
mysql> \. create_user.sql
mysql> \. create_tbl.sql
```

### Execute
You can add this task to crontab if you want to collect data once a day.
```
python atp/start_work.py
```

---


# ATP(低价机票采集)
这是一个用来抓取国内某知名网站机票数据的工具。

抓取从今天起60天内，国内所有航线的最低票价数据。

## 使用方法
### 创建数据库
```
cd db
mysql> .create_user.sql
mysql> .create_tbl.sql
```

### 执行脚本
```
python atp/start_work.py
```


##背景相关
###方案选择
####方案一
在做这个工具的时候，首选的方案是利用工具模拟用户的行为，逐天抓取机票价格数据，但是在实际执行的时候遇到了一些困难，平均1条航线抓取1天的数据大约需要10秒，而全国149个主要城市之间的航线有149 * 149=22201条，这样抓取所有航线60天的数据需要10 * 22201 * 60 = 13320600 =154天。所以这个方案目前来看还不可行，但是在性能好一些的机器上，将代码改造成多线程的方式之后，也许可行。

仿真用户用到的工具是casperjs，相关脚本在casperjs目录下，相关的使用方法可以在atp/start_work.searchOne中找到

atp/custom目录下定制了一些航线数据的收集

####方案二
使用一个更简单的方法，一次性抓取某条航线未来60天的最低票价(但是准确性可能差一些，依赖于网站数据的准确性)。目前采用本方案。

##进一步打算
利用这些抓取的数据，采用ML的方法做一些预测，譬如：  

* 假如我要购买北京到上海的在指定日期的机票，应该提前多少天购买最划算。

## TODO
1. 增加港澳台机票查询(返回的结果页面的tag与国内机票不同)

##Requirements
Python package:

*  MySQL-python
*  beautifulsoup4
*  lxml

casperjs








