from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url= "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn=urlopen(url)
raw_data= conn.read()
html_content = raw_data.decode('utf-8')
# with open('baitap3.html','wb') as f:
#     f.write(raw_data)
soup = BeautifulSoup(html_content,'html.parser')
ul=soup.find('div',style='overflow:hidden;width:100%;border-bottom:solid 1px #cecece;')
list_ul=ul.table.find_all('tr')
dataa=[]
sett=['đề mục','Quý 4-2016','Quý 1-2017','Quý 2-2017','Quý 3-1017']
for i in list_ul:
    td=i.find_all('td')
    dic={}
    for k in range(len(td)):
        if td[k].string!=None:
            if(k<5):
                dic[sett[k]]=td[k].string.strip()
    if dic!={}:
        dataa.append(OrderedDict(dic))
print(dataa)
pyexcel.save_as(records=dataa,dest_file_name="cty_suaVN.xlsx")


