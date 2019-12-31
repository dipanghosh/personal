#!/usr/bin/env python
# coding: utf-8

# In[4]:


from keras.models import load_model
import re
import requests
from bs4 import BeautifulSoup
import time, os
import urllib.request
from urllib.request import HTTPError, URLError
import numpy as np
from keras.preprocessing import image
import imageio
from tqdm import tqdm

model = load_model("aurora-model-0.2.h5")


# In[11]:


headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}

def get_processed_image(img, retry = 0):
    baseurl = 'http://nordlys.nipr.ac.jp/acaurora/Syowa/'
    try:
        t_image = imageio.imread(baseurl+img[2:]).reshape(720, 480, 3)
        return np.expand_dims(t_image,axis=0)
    except HTTPError as e:
        return None
    except Exception as e:
        print ("Shit went south, wait and retry", e)
        time.sleep(retry*retry+1)
        if retry < 3:
            return get_processed_image(img, retry=retry+1)
        else:
            print ("Tried Enough, Moving on now")
            return None

def day_predictions(date):
    site = 'http://nordlys.nipr.ac.jp/acaurora/Syowa/html/wrap.php?html='+str(date)+'.html'

    response = requests.get(site)

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img', src = re.compile(r'20'))
    imgs = [img['src'] for img in img_tags if not 'kog' in img['src']]

    predictions = []
    
    for img in tqdm(imgs):
        img = img[:-5]+".jpg"
        test_image = get_processed_image(img)
        if test_image is not None:
            result = model.predict(test_image)
            predictions.append((result)[0][0])
        else:
            print (img+" not found")
    return predictions


if __name__ == "__main__":
    pass


# In[12]:





# In[ ]:




