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
#载入HTML格式
    HTML = """
    <!doctype html>
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

    <head>
      <title>
      </title>
      <!--[if !mso]><!-->
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <!--<![endif]-->
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style type="text/css">
        #outlook a {
          padding: 0;
        }

        body {
          margin: 0;
          padding: 0;
          -webkit-text-size-adjust: 100%;
          -ms-text-size-adjust: 100%;
        }

        table,
        td {
          border-collapse: collapse;
          mso-table-lspace: 0pt;
          mso-table-rspace: 0pt;
        }

        img {
          border: 0;
          height: auto;
          line-height: 100%;
          outline: none;
          text-decoration: none;
          -ms-interpolation-mode: bicubic;
        }

        p {
          display: block;
          margin: 13px 0;
        }
      </style>
      <!--[if mso]>
            <noscript>
            <xml>
            <o:OfficeDocumentSettings>
              <o:AllowPNG/>
              <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
            </xml>
            </noscript>
            <![endif]-->
      <!--[if lte mso 11]>
            <style type="text/css">
              .mj-outlook-group-fix { width:100% !important; }
            </style>
            <![endif]-->
      <style type="text/css">
        @media only screen and (min-width:480px) {
          .mj-column-per-100 {
            width: 100% !important;
            max-width: 100%;
          }
        }
      </style>
      <style media="screen and (min-width:480px)">
        .moz-text-html .mj-column-per-100 {
          width: 100% !important;
          max-width: 100%;
        }
      </style>
      <style type="text/css">
        @media only screen and (max-width:480px) {
          table.mj-full-width-mobile {
            width: 100% !important;
          }

          td.mj-full-width-mobile {
            width: auto !important;
          }
        }
      </style>
    </head>

    <body style="word-spacing:normal;">
      <div style="">
        <!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
        <div style="margin:0px auto;max-width:600px;">
          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
            <tbody>
              <tr>
                <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                  <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:600px;" ><![endif]-->
                  <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                      <tbody>
                        <tr>
                          <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                              <tbody>
                                <tr>
                                  <td style="width:100px;">
                                    <img height="auto" src="https://www.onlyourmiracle.com/images/avatar.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="100" />
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </td>
                        </tr>
                        <tr>
                          <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                            <p style="border-top:solid 4px #F45E43;font-size:1px;margin:0px auto;width:100%;">
                            </p>
                            <!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" style="border-top:solid 4px #F45E43;font-size:1px;margin:0px auto;width:550px;" role="presentation" width="550px" ><tr><td style="height:0;line-height:0;"> &nbsp;
    </td></tr></table><![endif]-->
                          </td>
                        </tr>
                        <tr>
                          <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                            <div style="font-family:helvetica;font-size:20px;line-height:1;text-align:left;color:#F45E43;">
    """
    with open("./text.html", "w", encoding="utf-8") as f:
        f.write(HTML)
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

    flag = 0
    with open("./text.html", "a", encoding="utf-8") as f:
        for i in range(len(names)):
            if times[i] == today or times[i] == yesterday:
                news = "今日更新内容 :" + '<br/>' + '青岛大学教务处教务通知:' + names[i] + ',' + times[i] + ',' + links[i]
                f.write(news)
                f.write('<br/>')
                flag = 1
        if flag == 0:
            f.write('今天没有新的教务通知哦')
            f.write('<br/>')


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

    flag = 0
    with open("./text.html", "a", encoding="utf-8") as f:
        for i in range(len(names)):
            if times[i] == today or times[i] == yesterday:
                news = "今日更新内容 :" + '<br/>' + '青岛大学教务处教学动态:' + names[i] + ',' + times[i] + ',' + links[i]
                f.write(news)
                f.write('<br/>')
                flag = 1
        if flag == 0:
            f.write('今天没有新的教学动态哦')
            f.write('<br/>')

#获取每日人民日报PDF url
    with open("./text.html", "a", encoding="utf-8") as f:
        f.write('以下是今日人民日报PDF URL 轻触以查看')
        f.write('<br/>')
    today1 = datetime.datetime.now().strftime('%Y-%m/%d')
    today2 = datetime.datetime.now().strftime('%Y%m%d')

    for i in range(1, 5):
        url = 'http://paper.people.com.cn/rmrb/images/'+ today1 + '/0' + str(i) + '/rmrb' + today2 + '0' + str(i) + '.pdf'
        with open("./text.html", "a", encoding="utf-8") as f:
            f.write(url)
            f.write('<br/>')
        

#载入HTML格式
    HTML = """
    </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <!--[if mso | IE]></td></tr></table><![endif]-->
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <!--[if mso | IE]></td></tr></table><![endif]-->
      </div>
    </body>

    </html>
    """
    with open("./text.html", "a", encoding="utf-8") as f:
        f.write(HTML)
#更新相应内容
    with open("./update","w",encoding="utf-8") as f : 
        f.write("true")



    with open("./runtimes.txt", "r", encoding="utf-8") as f:
        x = f.read()

    x = str(int(x) + 1)
    with open("./runtimes.txt", "w", encoding="utf-8") as f:
        f.write(x)


    f.close()
    print("successful")
