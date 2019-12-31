#!/usr/bin/env python
# coding: utf-8

# In[1]:


#get_ipython().run_line_magic('run', 'predict.ipynb')
import predict as p

# In[2]:


from datetime import date, timedelta, datetime
import pandas as pd
from tqdm import tqdm
from csv_from_log import retrieve_pred_from_log
import os

def get_days(start, end):
    d1 = datetime.strptime(str(start), "%Y%m%d")
    d2 = datetime.strptime(str(end), "%Y%m%d")
    delta = d2 - d1         # timedelta
    return delta.days
    
def dateseq_gen(start, end):
    d1 = datetime.strptime(str(start), "%Y%m%d")
    d2 = datetime.strptime(str(end), "%Y%m%d")

    delta = d2 - d1         # timedelta

    for i in range(delta.days + 1):
        yield ((d1 + timedelta(i)).strftime("%Y%m%d"))


# In[ ]:


all_pred = {}

start = 20060201
end = 20071231

logfilepath = "pred-sweep-2006-2007.log"

def writelog(date, pred):
    logfile = open(logfilepath, "a")
    logfile.write(date+","+",".join(map(str,pred))+"\n")
    logfile.close()    


if os.path.isfile(logfilepath):
    os.remove(logfilepath)
def do_sweep():
    with tqdm(total = get_days(start, end)) as pbar:
        for date in dateseq_gen(start, end):
            pbar.set_description("Processing %s" % date)
            pred = p.day_predictions(date)
            all_pred[date] = pred
            writelog(date,pred)
            pbar.update()


df = pd.DataFrame.from_dict(all_pred, orient='index')
df.to_csv("2016.csv")
if __name__ == "__main__":
    do_sweep()
    #df = pd.DataFrame.from_dict(retrieve_pred_from_log(logfilepath), orient='index')
    #df.to_csv(logfilepath.split("-")[-1].replace(".log",".csv"))
