# coding:gbk
#2016/10/28
#默认result=True,删除from_encoding=x.encoding

import requests
from bs4 import BeautifulSoup
try:
    from urllib.parse import urlencode
except:
    print("Please Use Python3")
    exit()
import pickle

class EasyLogin():
    def __init__(self,cookie="",cookiefile=None,proxy=None):
        self.b = None
        self.s = requests.Session()
        self.s.headers.update({'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"})
        self.s.cookies.update(cookie)
        self.proxies={'http':proxy} if proxy is not None else None
        self.cookiefile='cookie.pickle'
        if cookiefile is not None:
            self.cookiefile = cookiefile
            try:
                self.s.cookies = pickle.load(open(cookiefile,"rb"))
            except:
                pass
                
    def showcookie(self):
        c = ""
        for i in self.s.cookies:
            c+= i.name+"="+i.value+";"
        return c
        
    def get(self,url,result=True):
        x = self.s.get(url,allow_redirects=False,proxies=self.proxies)
        if result: 
            if 'Location' in x.headers or len(x.text)==0: return False
            else:self.b = BeautifulSoup(x.text.replace("<br>","\n").replace("<BR>","\n"),'html.parser')
        return x.text
    
    def post_dict(self,url,dict,result=False,save=False):
        data = urlencode(dict)
        x = self.s.post(url,data,headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},allow_redirects=False,proxies=self.proxies)
        if save:  open(self.cookiefile,"wb").write(pickle.dumps(self.s.cookies))
        if result: self.b = BeautifulSoup(x.text,'html.parser')
        return x
    
    def post(self,url,data,result=False,save=False):
        x = self.s.post(url,data,headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},allow_redirects=False,proxies=self.proxies)
        if result: self.b = BeautifulSoup(x.text,'html.parser')
        if save:  open(self.cookiefile,"wb").write(pickle.dumps(self.s.cookies))
        return x
    
    def f(self,name,attrs):#find_all
        if self.b == None: return []
        return [i.text.replace('\r','').replace('\n','').replace('\t','').replace('  ','') for i in self.b.find_all(name,attrs=attrs)]
        
    def getList(self,searchString,elementName="a",searchTarget="href",returnType="href"):
        if self.b == None: return []
        result = []
        for element in self.b.find_all(elementName):
            #print(element)
            if searchString in element.get(searchTarget,""):
                result.append(element[returnType] if returnType!="element" else element)
        return result
