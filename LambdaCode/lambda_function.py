import boto3
import json

ec2 = boto3.client('ec2')
def lambda_handler(event, context):
    response = "Hello Swaraj@TR"
    return {"statusCode": 200, "body": json.dumps(response)}
