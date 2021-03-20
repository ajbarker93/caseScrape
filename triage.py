# Import libraries
import json
import os
from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

rootdir="/Users/adambarker/case_scrape"
os.chdir(rootdir)
os.listdir()

onlyfiles = [f for f in listdir(rootdir+"/summaries/") if isfile(join(rootdir+"/summaries/", f))]
onlyjsons = [f for f in onlyfiles if f.endswith('.json')]

len(onlyjsons)

# Set wildcards for selecting P1-1 cases
wildcards = ['1-1','P1','P1-1','P1-1-1','Protocol 1-1','Article 1','Article 1 al. 1 du Protocole','1 du Protocole n° 1']

results = pd.DataFrame(columns=['case', 'case_id','content','claimed','awarded'])

# Examine summaries and choose the list of P1-1 relevant cases
j = 0
for onlyjson in onlyjsons:
  try:
    with open(rootdir+"/summaries/"+onlyjson) as json_file: # first open the batches of summaries

      contents = json.load(json_file)
      contents2 = contents['results']

      for i in range(0,len(contents2)): # loop through each case in the batch
        j=j+1
        field_data = contents2[i]['columns']
        results = results.append({'case':field_data['docname'],'case_id':field_data['itemid'],'violation':field_data['violation'],'content':"",'claimed':"",'num_claimed':"",'awarded':"",'num_awarded':""},ignore_index=True)

        if (j % 200)==0:
            print(j)

  except:
    print("Error")

len(results)

print_success=0
k = 0

for id in results['case_id'].to_list():

  subf = id[-2:]

  filename = rootdir+'/docToText2/'+subf+'/'+id+'.txt'

  if isfile(filename):
    k = k+1
    f = open(filename, 'r') # read only
    contents = f.read()
    results.loc[results['case_id']==id,'content'] = contents

    if print_success:
      print('Successfully read ',id)

    if (k % 200)==0:
      print(k)

  else:
    print('No txt file for ',id)

print(len(results))
results.to_pickle("./results.pkl")
