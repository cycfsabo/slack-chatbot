import json
import boto3
client = boto3.client('ec2')

def lambda_handler(event, context):
    # TODO implement
    try:
        instances = list_instances()
        name = event["queryStringParameters"]["text"]
        state = get_state_instance(instances[name])
        message = "State of " + name + ": " + state
        return message
    except Exception as e:
        message = 'An exception occurred: ' + format(e)
        return message

def get_state_instance(instanceId):
    response = client.describe_instances(
        InstanceIds=[
            instanceId
            ]
        )
    return response['Reservations'][0]['Instances'][0]['State']['Name']

def list_instances():
    map={}
    response = client.describe_instances()
    instances = response['Reservations']
    for instance in instances:
        name = instance['Instances'][0]['Tags'][0]['Value']
        map[name] = instance['Instances'][0]['InstanceId']
    return map