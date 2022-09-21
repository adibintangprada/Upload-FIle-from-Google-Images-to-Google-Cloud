# Import needed libraries
from google.cloud import storage
import urllib.request

# Defining variables
project_id = 'data-fellowship-7-363107'
bucket_name = 'data_fellowship7'
source_file_name = 'https://ae01.alicdn.com/kf/He5af0c200eb345188c44345d7d649875Q.jpg_640x640Q90.jpg'
destination_blob_name = 'gundam_exia.jpg'
storage_client = storage.Client.from_service_account_json('credentials.json')

# Defining function for upload the file
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    file = urllib.request.Request(source_file_name, headers={'User-Agent': 'Mozilla/5.0'})   
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    name = urllib.request.urlopen(file).read()
    blob.upload_from_string(name, content_type='image/jpg')
    print("File uploaded in your cloud!")

# Run the function
upload_blob(bucket_name, source_file_name, destination_blob_name)