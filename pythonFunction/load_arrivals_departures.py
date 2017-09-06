from collections import OrderedDict
import csv
import json
import requests
import time
from collections import defaultdict

def load_matrices():
    reader = csv.reader(open('global_migrant_origin_database_version_4_with_total.csv', 'rU'), delimiter=',')
    row = reader.next()
    code_to_arrivals = {}
    code_to_departures = {}

    for row in reader:
        
        code_to_arrivals[row[0]]=row[228];
        code_to_departures[row[0]]=row[227];
 
                    
    f = open("code_to_arrivals.json",'w')
    f.write(json.dumps(code_to_arrivals))
    f.close()
    f = open("code_to_departures.json",'w')
    f.write(json.dumps(code_to_departures))
    f.close()
	
load_matrices()