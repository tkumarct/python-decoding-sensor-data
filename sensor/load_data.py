#Import os, glob, and csv
import os
import glob
import csv

#Create a Function to Parse the Data
def load_sensor_data():
    sensor_data=[]
    #Sensor Data File Management
    sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))
   
    print(sensor_files)
    #Read from data
    for sensor_file in sensor_files:
        with(open(sensor_file,'r')) as data_file:          
            data_reader=csv.DictReader(data_file, delimiter=',')
            #Load Data Records
            for row in data_reader:
                sensor_data.append(row)
    return sensor_data