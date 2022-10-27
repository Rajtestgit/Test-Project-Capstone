

import pandas as pd 
import json 
import collections 
from collections import defaultdict

# Function to Convert Html Table to Json file data.json 
def convert_html_json(table):
	df = pd.read_html(str(table))
	df[0].to_json('data.json', orient ='records')

	with open('data.json', 'r') as json_file:
		data = json.load(json_file)
	
	return data 

# Initialize a Dictionary  
time_slot = collections.defaultdict(list)

# Function To Create the Dictionary free time slot from Json File
def free_time_slots(data):
	for item in data:
		time = item.get('Time')
		for key, value in item.items():
 			if value == None:
 				key = key.split()
 				newKey=key[0]
 				time_slot[newKey].append(time)
	
	return time_slot

#list_value = free_time_slots(data)
#print(list_value)






 			
 		
