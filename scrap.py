from utils import *
import numpy as np
import json 
from tqdm import tqdm
import os

#City name must be valid
#do check the html page

city="Calgary"
# city="Toronto"
url="https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=&locationstring={city}".format(city=city)


#above code scraps jobIds from the html and loads them into numpy array 
#numpy array is stored in disk
try:
	job_id_arr=np.load("jobId_{city}.npy".format(city=city))
	print('jobId_{city}.npy'+'loaded from disk into memory'.format(city=city))
except:
      arr=press_button_multiple_times(url,delay=1.3)
      np.save("jobId_{city}.npy".format(city=city),arr)
      print('jobId_{city}.npy'+'stored into disk'.format(city=city))
      job_id_arr=np.load("jobId_{city}.npy".format(city=city))



#scraps the the data from job Id and stores it into JSON

data_arr = [
]
for i in tqdm(range(len(job_id_arr))):
    data=scarp_jd(job_id_arr[i])
    if data is not None:
         data_arr.append(data)


with open('data.json', 'w') as f:
    json.dump(data_arr, f, indent=4)  

