author = "Anindita"

import boto3
import glob

s3 = boto3.client('s3')

def uploadtoSourceData():
    counter = 1
    for file in glob.glob('Train/*.txt'):
        s3.upload_file(file, "sourcedatab00845637", str(counter) + '.txt')
        counter = counter + 1

uploadtoSourceData()
