import os
import moviepy.editor as mpe

basepath = "D:\\SDO_Data\\AIA_171"
dir_list = ["/".join((basepath, i)) for i in os.listdir(basepath)]

if not os.path.exists(basepath+"/movies"):
    os.mkdir(basepath+"/movies")
dir_list = ["/".join((basepath, i)) for i in os.listdir(basepath)]

for i in dir_list[2:]:
    base_dir = os.path.realpath(i)
    movie_name = i.split("/")[-1]
    print(base_dir)
    filenames=[base_dir +"\\"+ fname for fname in sorted(os.listdir(base_dir))]

    #print(directory)


    # Create video file from PNGs
    print("Producing video file...")
    filename  = os.path.join(os.path.realpath(basepath)+"\\movies\\"+movie_name+".mp4")
    if not os.path.isfile(filename):
        clip      = mpe.ImageSequenceClip(filenames, fps=24)
        clip.write_videofile(filename, threads=4, audio = False, progress_bar = False) 
        print("Done!")
    else:
        print ("Exists, Skipped")
    


# In[29]:


basepath = "./AuroraImages/2018"
pathlist = ["/".join((basepath, i)) for i in os.listdir(basepath)]


# In[30]:


os.path.realpath('./AuroraImages/2018/20180309')


# In[2]:



import os
from os import listdir
from PIL import Image
import moviepy.editor as mpe


# In[ ]:




