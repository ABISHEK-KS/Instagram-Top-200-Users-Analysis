import pandas as pd
import numpy as np
import pandas_profiling as pp


#-------------------------------------------------------------------
'''
ASK PHASE: 
Let us abbreviate Posts , followers , Avg likes , Engagement rate as 'PFAE'
The following points could be answered by analysis procedures:
1. PFAE Stats with respect to Channel info 
2. PFAE Stats according to category

These stats include average,max,min etc.
'''

#--------------------------------------------------------------------
#data pre-processing part

data=pd.read_csv('data.csv')
print(data.info())
print(data.describe)
print(data[data.isna().any(axis=1)])

b=pd.DataFrame(data)
c=b.dropna()
c.to_excel('Cxl.xlsx')

#now it's time to convert post values ( of the form xK) to x*1000 int values 
# and also to convert follower & avg likes in a similar fashion

cdata=pd.read_excel('Cxl.xlsx')
cdatadf=pd.DataFrame(cdata)
dflen=len(cdatadf)
newdflist=[]
rank=1
for k in range(dflen): 
    interiorlist=[]
    name=cdatadf['name'][k]
    cinfo=cdatadf['channel_Info'][k]
    category=cdatadf['Category'][k]
    engrate=cdatadf['Eng Rate'][k]  
    followerval=float(str(cdatadf['Followers'][k]).strip('M'))*1000000
    likeval=str(cdatadf['Avg. Likes'][k])
    postval=float(str(cdatadf['Posts'][k]).strip('K'))*1000   

    #Average likes has values with some cell values with 'K' and some without K.
    #so we run a conditional clauses
    if 'K' in likeval: 
        likeval=likeval.strip('K')
        likeval=float(likeval)
        likeval=likeval*1000
    else: 
        likeval=int(likeval)    

    #I tried to update the df using methods but that wasn't working. 
    #So I shall create a new DF.
    interiorlist.append(rank)
    interiorlist.append(name)
    interiorlist.append(cinfo)
    interiorlist.append(category)
    interiorlist.append(followerval)
    interiorlist.append(postval)
    interiorlist.append(likeval)
    interiorlist.append(engrate)
    rank+=1
    newdflist.append(interiorlist)
newdf=pd.DataFrame(newdflist,columns=['Rank','Name','Channel Info','Category','Followers','Posts','Avg Likes','Engagement rate'])    
print(newdf)
newdf.to_excel('FinalFile.xlsx')

#Building HTML profiling reports 

profrep=pp.ProfileReport(newdf)
profrep.to_file('index.html')
#----------------------------------------------------------------------------
#Please check the powerbi dashboard link for visualizations.









    
   
        


     