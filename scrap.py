from utils import *
import numpy as np
import json 
from tqdm import tqdm
import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


# use if required
def save_json_to_s3(data, bucket_name, file_name):
    s3_client = boto3.client('s3')
    json_data = json.dumps(data)
    try:
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=json_data, ContentType='application/json')
        print(f"File {file_name} uploaded to {bucket_name} successfully.")
    except (NoCredentialsError, PartialCredentialsError) as e:
        print("Credentials not available or incomplete. Please check your AWS credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")


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

    #break 100-100 into chunks

    os.makedirs('data', exist_ok=True)

    if i%100==0 and i!=0:
        file_name="data/data_{i}.json".format(i=i)
        if not os.path.isfile(file_name):
            with open('data/data_{i}.json'.format(i=i), 'w') as f:
                 json.dump(data_arr, f)  
            print('data_{i}.json saved into disk'.format(i=i))
        data_arr=[]

