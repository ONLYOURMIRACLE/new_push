# coding=utf-8
import requests
from lxml import etree
import datetime
today = datetime.datetime.now()
        # 计算偏移量
offset = datetime.timedelta(days=-1)
        # 获取想要的日期的时间
yesterday = (today + offset).strftime('%Y-%m-%d')
today = datetime.datetime.now().strftime('%Y-%m-%d')


if __name__ == '__main__':
#青岛大学教务处教务通知
    url = 'http://jw.qdu.edu.cn/homepage/infoArticleList.do;jsessionid=D7477658C10DEA783A4FB0410A47904D?columnId=358'

    response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'})
    response.encoding = response.apparent_encoding
    html = response.text
    parser = etree.HTML(html)


    titles = parser.xpath('//a[@target="_blank"]/text()')
    title = []
    for i in titles:
        for j in ['\r','\n',' ']:
            i = i.replace(j,'')
        title.append(i)


    names = []
    for i in title:
        if len(i) ==0:
            continue
        names.append(i)
    names = names[:-1]


    times = parser.xpath('//span/text()')
    times = times[2:-2]


    link = parser.xpath('//a[@target="_blank"]/@href')[:-1]
    links = []
    for i in link:
        links.append('http://jw.qdu.edu.cn/homepage/' + i)



    with open("./text.html", "w", encoding="utf-8") as f:
        if times[0] == today or times[0] == yesterday:
            news = "今日更新内容 :" + '\n' + '青岛大学教务处教务通知:' + names[0] + ',' + times[0] + ',' + links[0]
            f.write(news)
            f.write('\n')
        else:
            f.write('今天没有新的教务通知哦')
            f.write('\n')


#青岛大学教务处教学动态
    url = 'http://jw.qdu.edu.cn/homepage/infoArticleList.do;jsessionid=D7477658C10DEA783A4FB0410A47904D?sortColumn=publicationDate&columnId=5384&sortDirection=-1&pagingPage=1&pagingNumberPer=12'

    response = requests.get(url)
    response.encoding='utf-8'
    html = response.text
    parser = etree.HTML(html)


    titles = parser.xpath('//a[@target="_blank"]/text()')
    title = []  
    for i in titles:
        for j in ['\r','\n',' ']:
            i = i.replace(j,'')
        title.append(i)
    names = []
    for i in title:
        if len(i) ==0:
            continue
        names.append(i)
    names = names[:-1]


    times = parser.xpath('//span/text()')
    times = times[2:-2]


    link = parser.xpath('//a[@target="_blank"]/@href')[:-1]
    links = []
    for i in link:
        links.append('http://jw.qdu.edu.cn/homepage/' + i)


    with open("./text.html", "a", encoding="utf-8") as f:
        if times[0] == today or times[0] == yesterday:
            news = "今日更新内容 :" + '\n' + '青岛大学教务处教学动态:' + names[0] + ',' + times[0] + ',' + links[0]
            f.write(news)
            f.write('\n')
        else:
            f.write('今天没有新的教学动态哦')
            f.write('\n')


    with open("./update","w",encoding="utf-8") as f : 
        f.write("true")



    with open("./runtimes.txt", "r", encoding="utf-8") as f:
        x = f.read()

    x = str(int(x) + 1)
    with open("./runtimes.txt", "w", encoding="utf-8") as f:
        f.write(x)


    f.close()
    print("successful")
