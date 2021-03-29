import json
import boto3
client = boto3.client('ec2')

def lambda_handler(event, context):
    # TODO implement
    try:
        instances = list_instances()
        name = event["queryStringParameters"]["text"]
        #body = json.loads(event["body"])
        #name = body["text"]
        start_instances(instances[name])
        message = name + ' is started!' 
        return {
            'statusCode': 200,
            'body': message
        }
    except Exception as e:
        message = 'An exception occurred: ' + format(e)
        return message

        
def list_instances():
    map = {}
    response = client.describe_instances()
    instances = response['Reservations']
    for instance in instances:
        name = instance['Instances'][0]['Tags'][0]['Value']
        map[name] = instance['Instances'][0]['InstanceId']
    return map

def start_instances(instanceId):
    response = client.start_instances(
        InstanceIds=[
            instanceId,
        ],
    )