import requests
from bs4 import BeautifulSoup

url = 'https://dantri.com.vn/suc-khoe.htm'

# Lấy html từ trang cần lấy
response = requests.get(url)

# Tạo đối tượng soup từ html vừa lấy được
soup = BeautifulSoup(response.content, 'html.parser')

# Lấy tất cả các thẻ chứa các bài viết. Sử dụng thuộc tính chung là data-boxtype
post_elments = soup.find_all("div", {"data-boxtype": 'timelineposition'})

# In thử ra màn hình
for v in post_elments:
    print(v.a.attrs['title'])
    print(v.a.img.attrs['src'])

# Đưa kết quả vào 1 mảng các dict
result = []
for v in post_elments:
    result.append({'title': v.a.attrs['title'], 'src': v.a.img.attrs['src'], 'description': v.div.div.text.strip()})

# Lữu dữ liệu ra file json
# thông tin về json: https://freetuts.net/json-la-gi-cau-truc-chuoi-json-236.html
import json

with open('result.json', 'wt', encoding='utf-8') as f:
    f.write(json.dumps(result, ensure_ascii=False))

# Lữu dữ liệu ra file excel
# Nếu chưa cài pyexcel thì cân cài: python -m pip install pyexcel
# xong cài thêm python -m pip install pyexcel-xls
# link về pyexcel: http://docs.pyexcel.org/en/latest/
import pyexcel as p

p.save_as(records=result, dest_file_name="result.xls")