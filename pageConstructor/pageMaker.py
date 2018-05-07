import pageConstructor.pageconstructorClass as page
import os,platform

title = "Cherry Blossom: 2018"
desc = """  Cherry blossoms marks the coming of Spring, and it is very beautiful indeed. With improved gear and experience, I headed out to shoot these magnificent flowers this year. From wide angle to Macro, nothing was left out."""
folderName = "cherryblossom-2018"

myPage = page.galleryPage()
myPage.setinfo(title=title,desc=desc, keyw="Cherry Blossoms, Flower, Photography, Macro")
if "Windows" in platform.platform():
    myPage.path = "D:\Creative Cloud Files\portfolio_site\galleries\\"+folderName+"\\"
elif "Darwin" in platform.platform():
    myPage.path = "/Users/dghosh/Creative Cloud Files/portfolio_site/galleries/"+folderName+"/"


outfile = open(os.path.dirname(myPage.path) +"-generated.html", 'w')
outfile.write("\n".join(myPage.createPage()))