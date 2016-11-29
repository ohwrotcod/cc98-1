# cc98 Crawler

## Language
Python3

## Requirement
`pip install bs4 requests pymysql`

## Note
EasyLogin is another my project.


In this public version, credentials are hidden in config.py:

1. COOKIE: a dict of name and value in cookies

2. db(): return a database connection

example code for config.py:

    COOKIE = {'aspsky':'SOMETHING CREDIENTIAL','BoardList':'BoardID=Show',}

    def db():
        global conn
            conn = pymysql.connect(user='root',passwd='123456',host='localhost',port=3306,db='cc98',charset='utf8',init_command="set NAMES utf8")
            conn.encoding = "utf8"
            return conn


## Credits
https://github.com/aploium/mpms