# cc98 Crawler

## Language
Python3

## Requirement
`pip install bs4 requests pymysql`

## Note
EasyLogin is another my project.

`In this public version, credentials are hidden in config.py:
    COOKIE: a dict of name and value in cookies
    db(): return a database connection
        example:
        def db():
            global conn
            conn = pymysql.connect(user='root',passwd='123456',host='localhost',port=3306,db='cc98',charset='utf8',init_command="set NAMES utf8")
            conn.encoding = "utf8"
            return conn
`

## Credits
https://github.com/aploium/mpms