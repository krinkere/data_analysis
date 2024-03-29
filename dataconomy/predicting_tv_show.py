'''
Created on Jul 1, 2015

@author: alkrinker
'''
# Required Packages
#import csv
#import sys
#import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd
#from sklearn import datasets, linear_model
from sklearn import linear_model

# Function to get data
def get_data(file_name):
    data = pd.read_csv(file_name)
    flash_x_parameter = []
    flash_y_parameter = []
    arrow_x_parameter = []
    arrow_y_parameter = []
    for x1,y1,x2,y2 in zip(data['FLASH_EPISODE'],data['FLASH_US_VIEWERS'],data['ARROW_EPISODE'],data['ARROW_US_VIEWERS']):
        flash_x_parameter.append([float(x1)])
        flash_y_parameter.append(float(y1))
        arrow_x_parameter.append([float(x2)])
        arrow_y_parameter.append(float(y2))
    return flash_x_parameter,flash_y_parameter,arrow_x_parameter,arrow_y_parameter

# Function to know which Tv show will have more viewers
def more_viewers(x1,y1,x2,y2):
    regr1 = linear_model.LinearRegression()
    regr1.fit(x1, y1)
    predicted_value1 = regr1.predict(9)
    print predicted_value1
    regr2 = linear_model.LinearRegression()
    regr2.fit(x2, y2)
    predicted_value2 = regr2.predict(9)
    #print predicted_value1
    #print predicted_value2
    if predicted_value1 > predicted_value2:
        print "The Flash Tv Show will have more viewers for next week"
    else:
        print "Arrow Tv Show will have more viewers for next week"
        
x1,y1,x2,y2 = get_data('input_tv_data.csv')
print x1,y1,x2,y2
more_viewers(x1,y1,x2,y2)