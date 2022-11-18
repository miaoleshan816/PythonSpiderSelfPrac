import requests
from lxml import etree
#爬取的网站是147小说网
url='https://www.147xs.org/book/3722/55831.html'
i=1
sum=0
while (sum<=3):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
    resp=requests.get(url,headers)#发送请求
    # print(resp.text)
    e=etree.HTML(resp.text)#先用resp.txt，以etree.Html的形式解析，并赋值给e
    # etree.HTML()可以用来解析字符串格式的HTML文档对象，将传进去的字符串转变成_Element对象。
    title=e.xpath('//div[@class="bookname"]/h1/text()')[0]#解析出章节名,要注意h1下的text()，[0]是指[]里的文本内容,这里用e.xpath
    #print(title)#章节名
    info='\n'.join(e.xpath('//div[@id="content"]/p/text()'))#解析出章节内容,这边不能用+，否则会报错,这里得用.join()连接成为字符串，不然后面会报错
    #print(info)#文章内容
    sum = sum + i#这里准备用sum表示网页中的章节变化
    url='https://www.147xs.org/book/3722/5583'+str(sum)+'.html'#网址
    with open('斗罗大陆.txt','a',encoding='utf-8') as f:#打开斗罗大陆.txt，‘a’追加内容的形式，编码形式为‘utf-8’
          f.write(title+'\n'+info+'\n\n')# 写入文本文档，章节名title+章节内容info

