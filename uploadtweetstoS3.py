

import boto3

s3 = boto3.client('s3')
s3.upload_file('file_mongo_tweets.txt', "twitterdatab00845637", 'tweets.txt')


