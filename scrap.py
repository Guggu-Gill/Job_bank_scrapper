from utils import *
import numpy as np
import json 
from tqdm import tqdm
import os
import argparse

#ajust if required
delay_1=1.2
delay_2=0.6




parser = argparse.ArgumentParser(description='Job scraper for collecting job listings.')
parser.add_argument('--city', type=str, required=True, help='City for job listings, ensure its valid')
args = parser.parse_args()
city = args.city
print(f"Scraping job listings for city: {city}")

# city="Calgary"

url="https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=&locationstring={city}".format(city=city)


#above code scraps jobIds from the html and loads them into numpy array 
#numpy array is stored in disk
try:
	job_id_arr=np.load("jobId_{city}.npy".format(city=city))
	print('jobId_{city}.npy'+'loaded from disk into memory'.format(city=city))
except:
      arr=press_button_multiple_times(url,delay=delay_1)
      np.save("jobId_{city}.npy".format(city=city),arr)
      print('jobId_{city}.npy'+'stored into disk'.format(city=city))
      job_id_arr=np.load("jobId_{city}.npy".format(city=city))



#scraps the the data from job Id and stores it into JSON

data_arr = [
]
for i in tqdm(range(len(job_id_arr))):
    data=scarp_jd(job_id_arr[i],delay=delay_2)
    if data is not None:
         data_arr.append(data)

    #break 100-100 into chunks

    os.makedirs('data', exist_ok=True)

    if i%100==0 and i!=0:
        file_name="data/data_{i}.json".format(i=i)
        if not os.path.isfile(file_name):
            with open('data/data_{i}.json'.format(i=i), 'w') as f:
                 json.dump(data_arr, f)  
            print('data_{i}.json saved into disk'.format(i=i))
        data_arr=[]

