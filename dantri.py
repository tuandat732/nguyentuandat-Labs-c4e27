from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict #sắp xếp các giá trị trong dic khi vứt sang excel đúng theo thứ tự trong dic

#buoc 1: create connection
url = "https://dantri.com.vn"
conn = urlopen(url)

#1.1:down page
raw_data= conn.read()
html_content = raw_data.decode('utf-8')

#them
with open('dantri.html','wb') as f:
    f.write(raw_data)
#b2: find ROI
soup = BeautifulSoup(html_content,'html.parser')
ul = soup.find("ul",'ul1 ulnew') #gom ten thẻ và giá trị trong thuộc tính(nếu là class thì chỉ cần vứt giá trị vào trong "")

#b3: extract ROI
li_list = ul.find_all("li")
# print(li_list)
  #prettify la để in ra trình bày cho đẹp
# for li in li_list:
#     print(li.prettify())
#     print("*"*50)
# for li in li_list:
#     h4 = li.h4
#     a= h4.a

#     title=a.string
#     link= url +  a['href']
#     print(title.lstrip())
#     print(link)
#     print("*"*50)

#b4:save data
dataa=[]
for li in li_list:
    dic=OrderedDict({'title':li.h4.a.string.lstrip().rstrip(),'link':url+li.h4.a['href']})
    dataa.append(dic)
pyexcel.save_as(records=dataa,dest_file_name="dantri.xlsx")


