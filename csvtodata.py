# This file take the file excel file combined_csv and push it to the database 
#using mysql database
import pandas as pd #packge for working csv (read , write)

import os 
import mysql.connector as msql # packge for connection with mysql
from dotenv import load_dotenv
from mysql.connector import Error
import attendance 
# read the data from "combined_csv" file and put it in variable data

data = pd.read_csv('combined_csv.csv',index_col=False,delimiter=',' , usecols=['Name','summary'])
load_dotenv()
try:
#connect to mysql user
    conn = msql.connect(host=os.getenv("HOSTNAME_MYSQL"), user=os.getenv("USER_MYSQL"),
                        password=os.getenv("PASSWORD_MYSQL"))#give ur username, password
    if conn.is_connected(): # check if the connection is successful

# cusror is tool to help us for start working with mysql user 
        cursor = conn.cursor()
# cursor execute : running query in mysql
# check if db attendances found you can remove it from user .
       
        cursor.execute("DROP DATABASE IF EXISTS attendances")
# create new data base attendances
        cursor.execute("CREATE DATABASE attendances")
        print("Database is created")
# connect to db attendances
        conn.cmd_init_db("attendances")

        cursor=conn.cursor()
#
        cursor.execute('DROP TABLE IF EXISTS attendances_data;')
        print('Creating table....')

#create table attendance data with two culomns.
        cursor.execute("CREATE TABLE attendances_data(name varchar(255), attendance_summary varchar(255))")
      
        print("Table is created....")
        
# loop for the data from csv and insert into table "attendance_data"
# i =  index for the rows , row = the content for the row in data  
        for i, row in data.iterrows():
        
 # sql is query to insert the values to attendances_data      
            sql = "INSERT INTO attendances.attendances_data VALUES (%s,%s) "
            
            cursor.execute(sql, tuple(row))
            #print("Record inserted")
# save the changes we did
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)

def get_data() :
    sql="select * from attendances.attendances_data"
    cursor.execute(sql)
    
# fetchall = get the data from query we execute!!
    result = cursor.fetchall()
    for i in result:
        print(i)

    return result
    
    
    
    
    
    
    
    
    
    
    
    
    
