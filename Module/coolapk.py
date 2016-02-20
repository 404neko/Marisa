#coding: UTF-8
import requests
import os
import re


class Action:
    
    def __init__(self,text,env=None):
        self.env = env
        self.text = text

    def run(self):
        header = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36',
            }
        string = self.text
        session = requests.session()
        content = session.get(string).content
        info = content.split('apkDownloadUrl')[1]
        url_part = info.split('"')[1]
        package_name = url_part.split('=')[1][:-2]+'_'+url_part[-4:]
        header['Referer'] = string
        #print 'http://m.coolapk.com'+url_part
        respon = session.get('http://m.coolapk.com'+url_part+'',headers = header)
        #print respon.status_code
        f = open('Packs'+os.sep+package_name+'.apk','wb')
        f.write(respon.content)
        f.close()
        return {'value':package_name+'.apk','notice':['Coolapk','Download '+package_name+' end'],}

    @staticmethod
    def test(text):
        
        import re#http://ww4.sinaimg.cn/bmiddle/8245bf01jw1f13pjyynmvj20j6eu94qq.jpg
        return len(re.findall('http://m\.coolapk\.com/(game|apk)/.*',text))>0