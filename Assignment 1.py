# Import needed libraries
from google.cloud import storage
import urllib.request

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
