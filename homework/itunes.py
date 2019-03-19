from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url= "https://www.apple.com/itunes/charts/songs/"
conn=urlopen(url)
raw_data= conn.read()
html_content = raw_data.decode('utf-8')
soup = BeautifulSoup(html_content,'html.parser')
ull = soup.find("section",'section chart-grid')
am=ull.div.ul
list_ul=am.find_all('li')
dataa=[]
for i in list_ul:
    dic=OrderedDict({'name':i.h3.string,'artists':i.h4.string})
    dataa.append(dic)

pyexcel.save_as(records=dataa,dest_file_name="itunes.xlsx")

#part2
from youtube_dl import YoutubeDL
songs=[]
for i in dataa:
    song=i['name']+' '+i['artists']
    songs.append(song)
options = {
    'default_search': 'ytsearch',
    'max_downloads': len(songs), 
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(songs)




