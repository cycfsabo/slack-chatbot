import json
import boto3
client = boto3.client('ec2')

def lambda_handler(event, context):
    # TODO implement
    try:
        map = list_instances()
        
        return map
    except Exception as e:
        message = 'An exception occurred: ' + format(e)
        return message
    

def list_instances():
    map={"name":"id"}
    response = client.describe_instances()
    instances = response['Reservations']
    for instance in instances:
        name = instance['Instances'][0]['Tags'][0]['Value']
        map[name] = instance['Instances'][0]['InstanceId']
    return map