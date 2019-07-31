#-*-conding:utf-8-*-

import re
import requests

'''http://www.netbian.com/dongman/index.htm
<img src="http://img.netbian.com/file/2018/0501/76c26707a462f5e70b672b5db338e56d.jpg" alt="鬼刀风铃日落壁纸
">
<a href="/desk/20584.htm" title="鬼刀风铃日落壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0501/76c26707a462f5e70b672b5db338e56d.jpg" alt="鬼刀风铃日落壁纸"></a>
'''
def tiebaSpider(beginPage, endPage,url,header):

    for Page in range(beginPage,endPage+1):
        pn = int(Page - 1)
        if pn<1:
            fullurl = url + "index.htm"
        else:
            fullurl = url + "index_"+str(pn+1)+'.htm'
        filename = "第" + str(Page) + "页"
        print(fullurl)
        html = loadPage(fullurl, filename)
        url2 = re.findall('<a.*?href="/(desk/.*?.htm)"',html)

        urler = list(set(url2))
        urler.sort(key=url2.index)

        '''<a href="/desk/20584-1920x1080.htm" target="_blank"><img src="http://img.netbian.com/file/2018/0501/7bfb095480846b26e8fb392e3294ab28.jpg" alt="鬼刀风铃日落壁纸" title="鬼刀风铃日落壁纸"></a>'''
        for u in range(0,len(urler)):
            url3 = 'http://www.netbian.com/'+urler[u]

            html2 = loadPage2(url3, filename)
            url4 = re.findall('<div class="endpage".*?<a href="/(desk/.*?.htm)"',html2,re.S)
            if len(url4)>0:
                url5 = 'http://www.netbian.com/' + url4[0]

                html22 = loadPage2(url5, filename)

                tp = re.findall('<table id="endimg".*?src="(.*?.jpg)"',html22,re.S)
                if len(tp) > 0:

                    lsq = requests.get(tp[0],headers=header)
                    print(filename + '图片下载中')
                    with open('my/' +str(filename) + str(u) + '.jpg', 'wb') as f:
                                f.write(lsq.content)


def loadPage2(url,filename):
    print("下载中"+filename)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2767.400"}

    req = requests.get(url, headers=headers)
    req.encoding = 'gb2312'
    reqhtml = str(req.text)
    return reqhtml

def loadPage(url,filename):
    print("下载中"+filename)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2767.400"}

    req = requests.get(url, headers=headers)
    req.encoding = 'gb2312'
    reqhtml = str(req.text)
    return reqhtml


if __name__=="__main__":

    beginPage = input("请输入爬取的起始页(整数):")
    while True:
        #判断你输入的是否是数字
        if beginPage.isdigit():
            #是就给他变成int
            beginPage = int(beginPage)
            if beginPage <= 0:
                beginPage = 1
                break
            else:
                beginPage = int(beginPage)
                break
        else:
            beginPage = input("请输入爬取的起始页(整数):")
    endPage = int(input("请输入爬取的终止页："))
    url = 'http://www.netbian.com/dongman/'
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2767.400"

    }


    tiebaSpider(beginPage, endPage,url,header)