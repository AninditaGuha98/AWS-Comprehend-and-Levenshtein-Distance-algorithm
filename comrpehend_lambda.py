import json
import boto3


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    comprehend = boto3.client('comprehend')

    file_object = event["Records"][0]
    file = str(file_object['s3']['object']['key'])
    data = s3.get_object(Bucket='twitterdatab00845637', Key=file)

    contents = data['Body'].read(3000).decode('utf-8')
    # print("length",len(contents.encode('utf-8')))
    while contents:
        response = comprehend.detect_sentiment(Text=contents, LanguageCode='en')
        print(response)
        contents = data['Body'].read(3000).decode('utf-8')

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
