import time

import requests
from lxml import etree
import re
url='http://www.qiqixiaoshuo.com/book/6441/6467431.html'
while True:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
    resp = requests.get(url, headers)
    resp.encoding = 'gbk'  # 碰到乱码问题，经查询，编码为’gbk‘
    # print(resp.text)
    e = etree.HTML(resp.text)  # 解析
    title = e.xpath('//div[@class="bookname"]/h1/text()')[0]
    # print(title)
    info = '\n'.join(e.xpath('//div[@id="content"]/text()')).replace(u'\xa0', '')
    # 这里有发现解析下来的文件，在打印出来的时候，有\xao，经查询，用re库的replace方法解决
    # print(info)
    url1 = e.xpath('//div[@class="bottem1"]/a[4]/@href')[0]
    # 这边用/a[4]/@href表示对应下一章的网页链接，在最后面加上[0]是为了去除外面的[]
    # print(url1)
    url = 'http://www.qiqixiaoshuo.com' + str(url1)#将url1转化为字符串，并和网址连接在一起
    # print(url)
    with open('黑心女配修仙逆袭.txt', 'a', encoding='utf-8') as f:
        f.write(title + '\n' + info + '\n\n')  # 写入文档
    time.sleep(3)
    if url=='http://www.qiqixiaoshuo.com/book/6441/':#url指向最后一章时，退出循环
        break
