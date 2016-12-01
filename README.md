# cc98 Crawler

## Snapshot
![Snapshot](https://raw.githubusercontent.com/zjuchenyuan/cc98/master/doc/snapshot.jpg)

## Language
Python3

## Requirement
`pip3 install bs4 requests pymysql`

## Manual

To run this crawler, you need using screen and auto kill python3 processes

    #Don't forget to turn on the mysqld: `service mysqld start`(Centos) or `service mysql start`(Ubuntu)
    #I recommend you to `cp python3 pythoncc98`, and replace python3 to pythoncc98
    screen -S cc98
    while [ '1' = '1' ]; do python3 xinling.py; done
    # Press Ctrl+A C
    while [ '1' = '1' ]; do date; killall python3; sleep 666; done
    
If you give this python a parameter(boardid), it will get all post in this board

    python3 xinling.py 100 #get all post in "–£‘∞–≈œ¢"

## Note
EasyLogin is another my project.


In this public version, credentials are hidden in config.py:

1. COOKIE: a dict of name and value in cookies

2. db(): return a database connection

3. myip: randomly choose a source ip for tcp connection

example code for config.py:

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

## LICENSE
"Anyone But duanduan"(ABd) license

