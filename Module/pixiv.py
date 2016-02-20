#coding: UTF-8
import requests
import os
import re

class Action:
    
    def __init__(self,text,env=None):
        self.env = env
        self.text = text

    def run(self):
        session = requests.session()
        page_url = self.text
        respon = session.get(page_url)
        page = respon.content
        re_pic = '((http|https)://i[0-9]\.pixiv\.net/.*?/.*?x.*?/img-master/.*?(jpg|png|gif))'
        orig_url = re.findall(re_pic,page)[0][0]
        #<img src="http://i3.pixiv.net/c/600x600/img-master/img/2016/02/17/19/33/35/55341198_p0_master1200.jpg" alt="201501/HUG" title="201501/HUG" border="0">
        array = orig_url.split('/')
        array[-9] = 'img-original'
        array[-1] = '_'.join(array[-1].replace('.','_.').split('_')[:-2]+[array[-1].replace('.','_.').split('_')[-1]]).replace('_.','.')
        info = array[-9:]
        url = '/'.join(array[:3]+info)
        respon = session.get(url,headers = {'Referer':page_url})
        data = respon.content
        f = open('Packs'+os.sep+array[-1],'wb')
        f.write(data)
        f.close()
        return {'value':'Packs'+os.sep+array[-1],'notice':['Pixiv',array[-1]],}

    @staticmethod
    def test(text):
        import re#http://ww4.sinaimg.cn/bmiddle/8245bf01jw1f13pjyynmvj20j6eu94qq.jpg
        return len(re.findall('(http://ww[0-9]\.sinaimg\.cn/.*?/(jpg|png|gif))',text))>0
