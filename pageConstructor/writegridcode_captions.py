# -*- coding: utf-8 -*-
import sys
reload(sys)
from PIL import Image
from PIL.ExifTags import TAGS
import iptcinfo,os

descriptionFlag = False
def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    iptc = iptcinfo.IPTCInfo(fn)
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    ret["keywords"] = iptc.keywords
    if not descriptionFlag:
        ret['ImageDescription'] = ''
    return ret


#f = open("C:\Users\Dipan\Desktop\_MG_5223.jpg", 'rb')
#dirName = "D:\Creative Cloud Files\portfolio_site\galleries\\zugspitze\\"
#dirName = "D:\\Creative Cloud Files\\portfolio_site\\travels\\christmastrip2017\\vienna\\"
#outputFile = open(dirName+'outputHTML.html', 'w')



#print basename

#pprint(exifdata)

def getOutputHTML(f, dirName, gallery_title):
    filename = os.path.basename(f.name)
    basename = filename.split('-')[:-1]
    basename = '-'.join(basename)
    exifdata = get_exif(f)
    print exifdata['ImageDescription']
    outputHTML =  '<a href="./'+\
          dirName.split("\\")[-2]+\
          '/'+basename+\
          '-web.jpg" data-toggle="lightbox" data-gallery="' +gallery_title+ ' " data-footer= "'+\
          exifdata["ImageDescription"]+\
          '" ><figure class="photothumbnail"><img src="./'+\
          dirName.split("\\")[-2]+\
          '/thumb/'+basename+'-web-thumb.jpg" alt="'+\
          ','.join(exifdata['keywords'])+\
          '" class="center-block"></figure></a>'
    outputHTML = outputHTML.encode('latin-1').replace("ä","ae").replace("Ä","Äe").replace("ö","oe").replace("Ö","oe")
    return outputHTML

def imageGridCode(dirName, gallerytitle):
    html = []
    for filename in os.listdir(dirName):
        if filename.endswith('.jpg'):
            f = open(dirName + filename, 'rb')
        try:
            html.append(getOutputHTML(f, dirName, gallerytitle))
        except:
            pass

    return '\n'.join(html)

