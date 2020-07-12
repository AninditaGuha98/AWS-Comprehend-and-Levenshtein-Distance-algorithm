import json
import boto3


def lambda_handler(event, context):
    print(event)

    s3 = boto3.client('s3')
    comprehend = boto3.client('comprehend')

    file_object = event["Records"][0]
    file = str(file_object['s3']['object']['key'])
    data = s3.get_object(Bucket='twitterdatab00845637', Key=file)
    contents = data['Body'].read().decode('utf-8')

    contents_list = contents.split('RT @')
    for value in contents_list:
        response = comprehend.detect_sentiment(Text=value, LanguageCode='en')
        print(str(value), response['Sentiment'])

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
