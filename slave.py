import requests
from lxml import etree
import mongo_or
import redis_or
import master
import re
HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36","Accept":"*/*","Accept-Encoding": "gzip, deflate, br","X-Requested-With": "XMLHttpRequest","Referer": "https://www.xin.com/40d0nv9ky9/che68276154.html?channel=a49b117c44837d110753e751863f53","Connection": "keep-alive","Host": "www.xin.com"}

class Slave_Spisder():
    def parse_base_data(self,html):
        data=dict()
        model_name = html.xpath('//div[@class="cd_m_info cd_m_info_zjf"]/div[2]/div[1]/span/text()')[0].strip()
        data["车型名字"] = model_name
        car_mileage = html.xpath('//ul[@class="cd_m_info_desc"]/li[2]/a/text()')[0].strip()
        data["里程"] = car_mileage
        emission_stand = html.xpath('//ul[@class="cd_m_info_desc"]/li[3]/span[1]/text()')
        data["排放标准"] = emission_stand
        displa = html.xpath('//ul[@class="cd_m_info_desc"]/li[4]/span[1]/text()')
        data["排量"] =  displa
        raw_price = html.xpath('//p[@class="cd_m_info_price"]/span[2]/span/span/span/b/text()')
        getcar_time = html.xpath('//ul[@class="cd_m_info_desc"]/li[5]/span[1]/text()')
        data["车龄"] = getcar_time
        yearly_check_due = html.xpath('//div[@class="cd_m_i_pz"]/dl[1]/dd[4]/span[2]/text()')
        data["年检到期"] = yearly_check_due
        insurance_due = html.xpath('//div[@class="cd_m_i_pz"]/dl[1]/dd[5]/span[2]/text()')
        data["保险到期"] = insurance_due
        mainten_situ = html.xpath('//div[@class="cd_m_i_pz"]/dl[1]/dd[6]/span[2]/text()')
        data["保养情况"] = mainten_situ
        car_made = html.xpath('//div[@class="cd_m_i_pz"]/dl[2]/dd[1]/span[2]/a/text()')[0].strip()
        data["制造商"] = car_made
        car_mod = html.xpath('//div[@class="cd_m_i_pz"]/dl[2]/dd[2]/span[2]/a/text()')[0].strip()
        data["车型"] = car_mod
        color = html.xpath('//div[@class="cd_m_i_pz"]/dl[2]/dd[3]/span[2]/a/text()')[0].strip()
        data["颜色"] = color
        struct =html.xpath('//div[@class="cd_m_i_pz"]/dl[2]/dd[4]/span[2]/a/text()')[0].strip()
        data["车身结构"] = struct
        engin = html.xpath('//div[@class="cd_m_i_pz"]/dl[3]/dd[1]/span[2]/text()')
        data["发动机"] = engin
        transmiss = html.xpath('//div[@class="cd_m_i_pz"]/dl[3]/dd[2]/span[2]/a/text()')[0].strip()
        data["变速箱"] = transmiss
        fuel_mode = html.xpath('//div[@class="cd_m_i_pz"]/dl[3]/dd[4]/span[2]/text()')
        data["燃油类型"] = fuel_mode
        drive_mode = html.xpath('//div[@class="cd_m_i_pz"]/dl[3]/dd[5]/span[2]/text()')
        data["驱动形式"] = drive_mode
        fuel_consum = html.xpath('//div[@class="cd_m_i_pz"]/dl[3]/dd[6]/span[2]/text()')
        data["油耗"] = fuel_consum
        car_year = html.xpath('//ul[@class="cd_m_info_desc"]/li[1]/span[1]/text()')
        data["年份"] = car_year
        return data
    def get_base_fault_data(self,html):
        base_fault = dict()
        item1 = html.xpath('//div[@class="nor_abnormal"]/div[@class="nor_ab_head"]/span[1]/text()')
        base_fault["异常数目"] = item1
        item2 = html.xpath('//*[@id="cd_m_csg"]/div[2]/div[2]/div[2]/div[1]/div[2]/ul/li')
        fault_items = []
        for i in item2:
            li = i.xpath('text()')
            fault_items.extend(li)
        fault_items = [i.strip() for i in fault_items if not i.isspace()]
        base_fault["异常项目"] = fault_items
        return  base_fault
    def get_specil_fault_data(self):
        url = "http://www.xin.com/apis/ajax_report/get_chake_report/?carid=27341672"
        r = requests.get(url,headers = HEADERS)
        data = r.text
        city_id1 = data.encode("utf-8").decode("unicode_escape")
        city_id2 = eval(city_id1)
        return city_id2

if __name__ == '__main__':

    # A = master.Master_Spider("shenzhen")
    # html = A.get_html("http://www.xin.com/yrek41mkmg/che31211143.html")
    # C=Slave_Spisder()
    # C.get_specil_fault_data()
    # C.get_base_fault_data(html)
    url= "http://www.xin.com/yrek41mkmg/che73804094.html"
    import re
    pattern = re.compile(r'che(.*?).html')
    aaa = re.findall(pattern,url)[0]
    print(type(aaa))




