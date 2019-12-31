import pageconstructorClass as page
import os,platform

title = "Switzerland"
desc = """Photos from our trip to Switzerland in 2018"""
folderName = "switzerland"

myPage = page.galleryPage()
myPage.setinfo(title=title,desc=desc, keyw="Aurora Borealis, Aurora, Sweden, Abisko, North Pole")
if "Windows" in platform.platform():
    myPage.path = "C:\\Users\\dipan\\Creative Cloud Files\\portfolio_site\\travels\\" + folderName + "\\"
elif "Darwin" in platform.platform():
    myPage.path = "/Users/dghosh/Creative Cloud Files/portfolio_site/galleries/"+folderName+"/"


outfile = open(os.path.dirname(myPage.path) +"-generated-test.html", 'w')
outfile.write("\n".join(myPage.createPage()))