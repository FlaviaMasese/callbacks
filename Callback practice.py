#!/usr/bin/env python
# coding: utf-8

# # 10 lowest paid labour

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


LSMS=pd.read_csv(r'C:\Users\flavi\Downloads\data for practice\sect3_plantingw3.csv',low_memory=False)
LSMS


# In[9]:


#s3q21aHOW MUCH WAS YOUR LAST PAYMENT?(NAIRA) 
#s3q34aHOW MUCH WAS YOUR LAST PAYMENT?(NAIRA) 
LSMS.rename({'s3q13a':'labour_type', 's3q21a':'Income_earning'},inplace=True, axis='columns')


# In[18]:


LSMS.drop_duplicates(subset ='labour_type',keep = False, inplace = True) 


# In[19]:


LSMS.dropna(subset=['Income_earning'],inplace=True,)


# In[20]:


Labour_earning_Distr=(
LSMS.groupby(['labour_type'])['Income_earning']
.mean()
.reset_index()
.sort_values(by='Income_earning',ascending=True)
)
Ten_lowestPaidLabour=Labour_earning_Distr.nsmallest(n=10,columns=['Income_earning'])
Ten_lowestPaidLabour


# # Number of Individuals in each 10 lowest paid labour

# In[14]:


lowest_paid_labours = Ten_lowestPaidLabour['labour_type'].values
lowest_paid_labours

labour_earning_hhid = (
 LSMS.groupby(['indiv', 'hhid', 'labour_type'])['Income_earning']
    .mean()
    .reset_index()
    .sort_values(by='Income_earning', ascending=True)
)

for i in lowest_paid_labours:
    low_select = labour_earning_hhid[labour_earning_hhid['labour_type'] == i]
    househould_low_count = low_select['hhid'].count()
    indiv_low_count = low_select['indiv'].count()

    print(f'{househould_low_count} households with {indiv_low_count} persons are {i} ')


# # Highest paid professions

# In[16]:


Labour_earning_Distr=(
LSMS.groupby(['labour_type'])['Income_earning']
.mean()
.reset_index()
.sort_values(by='Income_earning',ascending=True)
)
Ten_highestPaidLabour=Labour_earning_Distr.nlargest(n=10,columns=['Income_earning'])
Ten_highestPaidLabour


# # Number of Individuals in each 10 highest paid labour

# In[21]:


highest_paid_labours = Ten_highestPaidLabour['labour_type'].values
highest_paid_labours

labour_earning_hhidd = (
 LSMS.groupby(['indiv', 'hhid', 'labour_type'])['Income_earning']
    .mean()
    .reset_index()
    .sort_values(by='Income_earning', ascending=True)
)

for i in highest_paid_labours:
    high_select = labour_earning_hhidd[labour_earning_hhidd['labour_type'] == i]
    househould_high_count = high_select['hhid'].count()
    indiv_high_count = high_select['indiv'].count()

    print(f'{househould_high_count} households with {indiv_high_count} persons are {i} ')


# In[45]:


import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Output, Input, State
import plotly.graph_objs as go
from jupyter_dash import JupyterDash
import dash_trich_components as dtc


# In[ ]:


colors=['black','blue','red','yellow','pink''orange']
app= dash.Dash(__name__)
app.layout = html.Div(
                      children=[
                          dcc.Dropdown(id='my_dropdown', multi=True,
                                      options=[{'label':x, 'value':x}for x in sorted(LSMS.labour_type.unique())],
                                      value=['EDUCATION (ZONAL OFFICER)','HOSPITAL CLEANER/ATTENDANT'])
                      ])

