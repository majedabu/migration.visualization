# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 15:00:22 2017

@author: sd
"""

import json

world = json.loads(open("code_to_coordinates.json").read())
raduis1=json.loads(open("code_to_arrivals.json").read())
raduis2=json.loads(open("code_to_departures.json").read())
max_arriv=34634797
max_depar=12098617
res = {}
res1={}

for feature in world :
     print int(raduis1[feature])
     res[feature]=[world[feature][0],world[feature][1],float(raduis1[feature])/max_arriv*100];
     res1[feature]=[world[feature][0],world[feature][1],float(raduis2[feature])/max_depar*100];

    

#print res
f = open("code_To_raduis_arravil.json",'w')
f.write(json.dumps(res))
f.close()
f = open("code_To_raduis_departures.json",'w')
f.write(json.dumps(res1))
f.close()
