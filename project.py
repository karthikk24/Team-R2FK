import csv
import matplotlib.pyplot as plt
import requests
import pandas as pd
import numpy as np
from pprint import pprint
from config import api_key1, api_key2

name_page =[]
danger = []


url = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=gzBvVGiFEKMOUKe2a3RX0xNX9RPoGbz1x53zQSN1"
units = "metric"

response=requests.get(url).json()
pprint(response)



name_page = []
danger = []
abs_mag = []
while_break = []

# below is the code to loop through the individual pages, and make lists of some of the various information we are looking to pull out,
# I am still trying to work on switching out API's in the middle of the request. I do not recommend running it because it will lock out the API for an hour.


#while url:
#    response = requests.get(url).json()
#    for x in range(len(response['near_earth_objects'])):
#        name_page.append(response['near_earth_objects'][x]['name'])
#        danger.append(response['near_earth_objects'][x]['is_potentially_hazardous_asteroid'])
#        abs_mag.append(response['near_earth_objects'][x]['absolute_magnitude_h'])    
#url = response['links'].get('next')

astroid_df = pd.DataFrame(
    {'Name': name_page,
     'Is Potentially Hazardous': danger,
     'Absolute Magnitude': abs_mag,
    })
