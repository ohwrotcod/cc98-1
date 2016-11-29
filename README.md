# cc98 Crawler

## Snapshot
![Snapshot](https://raw.githubusercontent.com/zjuchenyuan/cc98/master/doc/snapshot.jpg)

## Language
Python3

## Requirement
`pip install bs4 requests pymysql`

## Manual

To run this crawler, you need using screen and auto kill python3 processes

    #Don't forget to turn on the mysqld: `service mysqld start`(Centos) or `service mysql start`(Ubuntu)
    #I recommend you to `cp python3 pythoncc98`, and replace python3 to pythoncc98
    screen -S cc98
    while [ '1' = '1' ]; do python3 xinling.py; done
    # Press Ctrl+A C
    while [ '1' = '1' ]; do date; killall python3; sleep 666; done
    


## Note
EasyLogin is another my project.


In this public version, credentials are hidden in config.py:

1. COOKIE: a dict of name and value in cookies

2. db(): return a database connection

example code for config.py:

    #Example Code for config.py
    COOKIE = {'aspsky':'SOMETHING CREDIENTIAL','BoardList':'BoardID=Show',}
    def db():
        global conn
        conn = pymysql.connect(user='root',passwd='123456',host='localhost',port=3306,db='cc98',charset='utf8',init_command="set NAMES utf8")
        conn.encoding = "utf8"
        return conn


## Credits
https://github.com/aploium/mpms