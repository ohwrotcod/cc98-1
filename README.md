# cc98 Crawler

## Snapshot
![Snapshot](https://raw.githubusercontent.com/zjuchenyuan/cc98/master/doc/snapshot.jpg)

## Language
Python3

## Requirement

本爬虫依赖的EasyLogin库需要安装BeautifulSoup和requests才能运行

`pip3 install bs4 requests pymysql`

## Manual

To run this crawler, you need using screen and auto kill python3 processes

目前的版本在完成抓取任务后不会自动退出，需要定时kill，建议在screen中执行

    screen -S cc98
    while [ '1' = '1' ]; do python3 xinling.py; done
    # Press Ctrl+A C
    while [ '1' = '1' ]; do date; killall python3; sleep 666; done
    
If you give this python a parameter(boardid), it will get all post in this board

不带参数地运行就会抓取十大+最新发帖，指定一个版块ID的参数则会抓取本版块所有发帖

    python3 xinling.py 100 #get all post in "校园信息"

## Note
[EasyLogin is another my project.](https://github.com/zjuchenyuan/EasyLogin) ←_← 还不快戳戳，求Star咯

Don't forget to turn on the mysqld: `service mysqld start`(Centos) or `service mysql start`(Ubuntu)

数据库还是要能连上的，建表的操作是自动的，不需要执行额外的sql文件

In this public version, credentials are hidden in config.py:

嗯哼，敏感的信息当然不会丢到github上啦

1. COOKIE: a dict of name and value in cookies

2. db(): return a database connection

3. myip: randomly choose a source ip for tcp connection, you need to obtain these ip first ^.^

example code for config.py:

你需要写一个config.py哟~

    #Example Code for config.py
    import random,pymysql
    COOKIE = {'aspsky':'SOMETHING CREDIENTIAL','BoardList':'BoardID=Show',}
    def db():
        global conn
        conn = pymysql.connect(user='root',passwd='123456',host='localhost',port=3306,db='cc98',charset='utf8',init_command="set NAMES utf8")
        conn.encoding = "utf8"
        return conn
    myip='10.1.2.{}'.format(random.randint(66,99))  #randomly choose a source ip for crawler


## Credits
https://github.com/aploium/mpms

ym一下Aploium大佬

## LICENSE
"Anyone But duanduan"(ABd) license

