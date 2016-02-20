#coding: UTF-8
import requests
import os
import re
import socket 

class Action:
    
    def __init__(self,text,env):
        self.env = env
        self.text = text

    def proxy(self,port = 1080):
        def scan(port):
            s = socket.socket()
            if s.connect_ex(('localhost', port)) == 0:
                s.close()
                return True
            return False
        if scan(port):
            import socks
            socks.set_default_proxy(socks.SOCKS5, 'localhost', 1080, rdns=True)
            socket.socket = socks.socksocket
            return True
        else:
            return False
              
        

    def run(self):
        if self.proxy():
            re_get_pic = 'data-image-url="((https|http)://pbs.twimg.com/media/.*?.(jpg|png|gif))"'
            print 1
            s_url = re.findall(re_get_pic,requests.get(self.text,verify=False).content)[0]
            url = s_url+':orig'
            print 2
            data = requests.get(url,verify=False)
            f = open(s_url.split('/')[-1],'wb')
            f.write(data.content)
            f.close()
            return {'value':url,'notice':['twitter','Picture has been downloaded.'],}
        else:
            f = open('record.txt','a+')
            f.write(self.text)
            f.write('\n')
            f.close()
            return {'value':'','notice':['twitter','No proxy, url has been recorded.'],}


    @staticmethod
    def test(text):
        import re
        return len(re.findall('((https|http)://twitter.com/.*?/status/.*?)',text))>0