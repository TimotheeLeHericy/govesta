
import pandas as pd
import numpy as np
import requests
import json
from sqlalchemy import create_engine
import schedule
import time


# In[3]:


# Script for getting and cleanning ads to be schedule
def ads_govesta():
	df_tr = pd.read_csv('C:/Users/timo2/Documents/Projet_3/ads_5villes_tr_v01.csv')
	    # Credentials to database connection
    hostname="151.80.148.247"
    dbname="govesta_db"
    uname="root"
    pwd="govesta64"

    # Create SQLAlchemy engine to connect to MySQL Database
    engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                    .format(host=hostname, db=dbname, user=uname, pw=pwd), max_overflow=-1)

    # Convert dataframe to sql table
    df_tr.to_sql('govesta_test', engine, index=False, if_exists='replace')


# In[ ]:


schedule.every(60).seconds.do(ads_govesta)

while True:
    schedule.run_pending()
    time.sleep(1)
