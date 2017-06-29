import re
import numpy as np
import pandas as pd
import scipy as sc

def align(pathSensData, pathAct):
    sensor_set = pd.read_csv(pathSensData, sep='\s+', parse_dates=[['Start', 'time'], ['End', 'time.1']])
    activities_set = pd.read_csv(pathAct, sep='\s+', parse_dates=[['Start', 'time'], ['End', 'time.1']])
    return sensor_set[1:], activities_set[1:]

def main():
    sensor_set, activities_set = align('inc/OrdonezA_Sensors.txt', 'inc/OrdonezA_ADLs.txt')
    sensor_set.to_csv(r'no_blankSensors.txt', header=None, index=None, sep=' ', mode='a')
    activities_set.to_csv(r'no_blankActivities.txt', header=None, index=None, sep=' ', mode='a')
    print(sensor_set)
    print(activities_set)