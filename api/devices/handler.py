import json
import boto3
from botocore.exceptions import ClientError

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')
table_name = 'Device'

def lambda_handler(event, context):
    http_method = event['requestContext']['http']['method']
    
    if http_method == 'POST':
        return create_device(event)
    elif http_method == 'GET':
        return get_device(event)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Unsupported HTTP method'})
        }

def create_device(event):
    try:
        body = json.loads(event['body'])
        required_fields = ['id', 'deviceModel', 'name', 'note', 'serial']
        
        # Check if all required fields are present in the request
        for field in required_fields:
            if field not in body:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': f'Missing field: {field}'})
                }
        
        # Save the device data to DynamoDB
        dynamodb.put_item(
            TableName=table_name,
            Item={
                'id': {'S': body['id']},
                'deviceModel': {'S': body['deviceModel']},
                'name': {'S': body['name']},
                'note': {'S': body['note']},
                'serial': {'S': body['serial']}
            }
        )
        
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Device created successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def get_device(event):
    try:
        device_id = event['pathParameters']['id']
        
        response = dynamodb.get_item(
            TableName=table_name,
            Key={
                'id': {'S': device_id}
            }
        )
        
        item = response.get('Item')
        
        if item:
            device = {
                'id': item['id']['S'],
                'deviceModel': item['deviceModel']['S'],
                'name': item['name']['S'],
                'note': item['note']['S'],
                'serial': item['serial']['S']
            }
            
            return {
                'statusCode': 200,
                'body': json.dumps(device)
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Device not found'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
