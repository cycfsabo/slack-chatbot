import json
import boto3
client = boto3.client('events')
arn = 'arn:aws:lambda:us-east-2:700712043529:function:start_instances'

def lambda_handler(event, context):
    try:
        # TODO implement
        value = list(event["queryStringParameters"]["text"].split(","))
        rule_name = value[0]
        cron_expression = value[1]
        create_rule(rule_name,cron_expression)
        response = create_target(rule_name,arn)
        message = 'Created rule ' + rule_name + ' with target is Lambda function: start_instances'
        return {
            'body': message
        }
    except Exception as e:
        message = 'An exception occurred: ' + format(e)
        return {
            'body': message
        }

def create_rule(name,cron_expression):
    response = client.put_rule (
        Name=name,
        ScheduleExpression=cron_expression,
        State='ENABLED'
    )
    return response

def create_target(rule_name, arn):
    response = client.put_targets(
        Rule=rule_name,
        Targets=[
            {
                'Id':'hungcao19',
                'Arn':arn
            }]
        )
    return response
    
