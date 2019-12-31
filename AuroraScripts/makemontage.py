
# coding: utf-8

# In[1]:


from PIL import Image
import os
import io
import re, requests
import urllib.request
from PIL import Image, ImageDraw
from bs4 import BeautifulSoup
from tqdm import tqdm

def make_contact_sheet(PIL_images,ncols=10,nrows=1,photow=72,photoh=48,marl=0,mart=0,marr=0,marb=0,padding=5):
    """    Make a contact sheet from a group of filenames:

    fnames       A list of names of the image files
    
    ncols        Number of columns in the contact sheet
    nrows        Number of rows in the contact sheet
    photow       The width of the photo thumbs in pixels
    photoh       The height of the photo thumbs in pixels

    marl         The left margin in pixels
    mart         The top margin in pixels
    marr         The right margin in pixels
    marb         The bottom margin in pixels

    padding      The padding between images in pixels

    returns a PIL image object.
    """
    #calculate rows
    nrows = (len(PIL_images)//ncols)+1

    # Calculate the size of the output image, based on the
    #  photo thumb sizes, margins, and padding
    marw = marl+marr
    marh = mart+ marb

    padw = (ncols-1)*padding
    padh = (nrows-1)*padding
    isize = (ncols*photow+marw+padw,nrows*photoh+marh+padh)

    # Create the new image. The background doesn't have to be white
    white = (255,255,255)
    inew = Image.new('RGB',isize,white)

    count = 0
    # Insert each thumb:
    for irow in range(nrows):
        for icol in range(ncols):
            left = marl + icol*(photow+padding)
            right = left + photow
            upper = mart + irow*(photoh+padding)
            lower = upper + photoh
            bbox = (left,upper,right,lower)
            try:
                # Read in an image and resize appropriately
                img = PIL_images[count].resize((photow,photoh))
            except:
                break
            inew.paste(img,bbox)
            count += 1
            
    return inew


# In[2]:


headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}

def getPIL_image(img_url):
    try:
        request_= urllib.request.Request(img_url,None,headers)
        response = urllib.request.urlopen(request_)
        i = Image.open(io.BytesIO(response.read()))    
    except:        
        i = Image.new('RGB',(72,48),(255,255,255))
        d = ImageDraw.Draw(i)
        d.text((1,10), "Link Broken", fill=(0,0,0))
    return i
    


# In[3]:


def make_date_montage(date):
    date = str(date)
    year = date[0:4]
    site = 'http://nordlys.nipr.ac.jp/acaurora/Syowa/html/wrap.php?html='+date+'.html'
    baseurl = 'http://nordlys.nipr.ac.jp/acaurora/Syowa/'

    response = requests.get(site)

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img', src = re.compile(r'20'))

    imgs = [img['src'] for img in img_tags if not 'kog' in img['src']]

    PIL_images = []

    for img in tqdm(imgs):
            #img = img[:-5]+".jpg"
            PIL_images.append(getPIL_image (baseurl+img[2:]))
    montage = make_contact_sheet(PIL_images)
    montage.save("datemontages/"+year+"/"+date+"-montage.jpg")


# In[4]:

year = "2013"

import pandas as pd
df=pd.read_csv("processed_preds/"+year+"_processed.csv", index_col=False)
selDates = df.loc[df['sum'] >= 2].iloc[:, 1]

# In[7]:


for date in tqdm(selDates):
    if not os.path.isfile("datemontages/"+year+"/"+str(date)+"-montage.jpg"):
        make_date_montage(date)
    else:
        print ("File Exists, Skipped")

