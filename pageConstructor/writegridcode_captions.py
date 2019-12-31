import sys
from PIL import Image
from PIL import IptcImagePlugin
import os

descriptionFlag = False


def get_title_description(image):
    im = Image.open(image)
    iptc = IptcImagePlugin.getiptcinfo(im)
    infodict = {}
    try:
        infodict["title"] = iptc.get((2,5)).decode()
    except (AttributeError):
        infodict["title"] = ""
    try:
        infodict["description"] = iptc.get((2,120)).decode()
    except (AttributeError):
        infodict["description"] = ""
    try:
        infodict["photographer"] = iptc.get((2,80)).decode()
    except (AttributeError):
        infodict["photographer"] = "Dipan"
    try:
        keywordlist = iptc.get((2,25))
        templist = []
        if keywordlist:
            for keyword in keywordlist:
                templist.append(keyword.decode())
            infodict["keywords"] = ", ".join(templist)
        else:
            infodict["keywords"] = ""
    except (AttributeError):
        infodict["keywords"] = ""
    return infodict

def getOutputHTML(f, dirname, gallery_title):
    local_dirname = dirname.split("\\")[-2]
    filename = os.path.basename(f.name)
    basename = filename.split('-')[:-1]
    original_filename = '-'.join(basename)
    exifdata = get_title_description(f.name)
    print(exifdata)
    href = "./{}/{}-web.jpg".format(local_dirname, original_filename)
    src = "./{}/thumb/{}-thumb.jpg".format(local_dirname, original_filename)

    outputHTML =  '<a href="{}" data-toggle="lightbox" data-gallery="{}" data-footer= "{}" ><figure class="photothumbnail"><img src="{}" alt="{}" class="center-block"></figure></a>'.format(href, gallery_title, exifdata["description"], src, exifdata["keywords"])

    return outputHTML

def imageGridCode(dirName, gallerytitle):
    html = []
    for filename in os.listdir(dirName):
        if filename.endswith('.jpg'):
            f = open(dirName + filename, 'rb')
            html.append(getOutputHTML(f, dirName, gallerytitle))


    return '\n'.join(html)