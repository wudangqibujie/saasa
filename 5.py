import requests
from lxml import etree

url = "http://www.xin.com/yrek41mkmg/che27341672.html"
r = requests.get(url)
html = etree.HTML(r.text)
itm = html.xpath('/html/body/div[2]/div[13]/div/div[4]/div[1]/dl[2]/dd/span[2]/text()')
# f = open("bmwwww.html","w",encoding="utf-8")
# f.write(r.text)
# f.close()
print(itm)
