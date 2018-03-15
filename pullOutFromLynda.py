import urllib
from bs4 import BeautifulSoup as bs
import re
url = \
"https://www.lynda.com/Photoshop-tutorials/Photoshop-CC-2017-One-One-Mastery/497777-2.html"
soup = bs(urllib.urlopen(url), "html.parser")
video_list= [re.sub('\s+',' ',link.string).encode('utf-8').strip() for link in soup.findAll('h4', class_="ga")]
print video_list

file = open("C:\Users\Dipan\Desktop\PsAndAiTeaching\PSImpList.txt", 'a')
file.write("\n".join(video_list))
file.write("\n")
file.close()