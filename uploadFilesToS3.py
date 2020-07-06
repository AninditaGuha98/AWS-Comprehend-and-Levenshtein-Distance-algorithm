author = "Anindita"

import boto3
import glob
import time

s3 = boto3.client('s3')

def uploadtoSourceData():
    counter = 1
    for file in glob.glob('Train/*.txt'):
        s3.upload_file(file, "sourcedatab00845637", str(counter) + '.txt')
        print("upload successful", counter)
        input()
        counter = counter + 1
        time.sleep(0.1)
