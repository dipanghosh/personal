# -*- coding: utf-8 -*-
import sys
reload(sys)
from PIL import Image
from PIL.ExifTags import TAGS
from pprint import pprint
import iptcinfo,os

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    iptc = iptcinfo.IPTCInfo(fn)
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    ret["keywords"] = iptc.keywords
    return ret


#f = open("C:\Users\Dipan\Desktop\_MG_5223.jpg", 'rb')
dirName = "C:\Users\Dipan\Creative Cloud Files\portfolio_site\christmastrip2017\\praha\\"
outputFile = open(dirName+'outputHTML.html', 'w')



#print basename

#pprint(exifdata)

def getOutputHTML(f):
    filename = os.path.basename(f.name)
    basename = filename.split('-')[:-1]
    basename = '-'.join(basename)
    exifdata = get_exif(f)
    outputHTML =  '<a href="./'+\
          dirName.split("\\")[-2]+\
          '/'+basename+\
          '-web.jpg" data-toggle="lightbox" data-gallery="christmasmarket" data-footer= "'+\
          exifdata["ImageDescription"]+\
          '" ><figure class="photothumbnail"><img src="./'+\
          dirName.split("\\")[-2]+\
          '/thumb/'+basename+'-web-thumb.jpg" alt="'+\
          ','.join(exifdata['keywords'])+\
          '" class="center-block"></figure></a>'
    outputHTML = outputHTML.encode('latin-1').replace("ä","ae").replace("Ä","Äe").replace("ö","oe").replace("Ö","oe")
    return outputHTML

for filename in os.listdir(dirName):
    f = open(dirName + filename, 'rb')
    try:
        outputFile.write(getOutputHTML(f))
        outputFile.write('\n')
    except:
        pass

