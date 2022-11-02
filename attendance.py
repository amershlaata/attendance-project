#!/usr/bin/python
""" calculate attendance based on webex csv files"""

import os 
import glob
import pandas as pd
import sys
from dotenv import load_dotenv
#protocol for connection with ip server.(pysftp)
import pysftp
cnopts = pysftp.CnOpts()
cnopts.hostkeys=None

load_dotenv()

#we make connection with server 185.164.16.144
with pysftp.Connection('185.164.16.144' , username=os.getenv("USERNAME_SFTP"), password=os.getenv("PASS_SFTP"),cnopts= cnopts) as sftp:

# check if we have dirctory "csv_files" on my ubuntu
	if not os.path.exists('./csv_files'):
		os.mkdir('csv_files')
	sftp.get_d('/var/tmp/csv_files','./csv_files',preserve_mtime=True)
		
j=0

for i in glob.glob('./csv_files/*.csv'):
	
	#print(i)
#we read the csv files on columns name , attendance...
	df = pd.read_csv(i, encoding="UTF-16LE" , sep="\t",          												usecols=['Name' , 'Attendance Duration'])
	df['Name']=df['Name'].str.lower()
	
	
	df['Attendance Duration']=df['Attendance Duration'].str.split().str[0].astype('int64')
#group the data by name and sum the attendance duraion tha related to the same name 
	df=df.groupby('Name' , as_index=False)['Attendance Duration'].sum()
	j+=1
		
	column_name="Attendance_" + j.__str__()
	df.rename(columns={"Attendance Duration": column_name} ,			inplace=True)
	if j==1:
		output=df
		continue
	output=pd.merge(output,df,on='Name',how='outer')
		
col_array=output.filter(like='Attendance').columns.tolist()
output['summary']=output[col_array].sum(axis=1)
#print(output)
		
output.to_csv("combined_csv.csv",index = False ) 		
		
			
		
