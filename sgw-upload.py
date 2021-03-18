import json
import urllib.parse
import boto3
s3 = boto3.client('s3')
def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    # Get the bucket name and key name from the event
    bucket = event.get('detail').get('bucket-name')
    key = event.get('detail').get('object-key')
    
    # add the tag Expire=True
    try:
        print('Putting Tag for object {} from bucket {}'.format(key, bucket))
        response = s3.put_object_tagging(
            Bucket=bucket,
            Key=key,
            Tagging={
                'TagSet': [
                    {
                        'Key': 'Month',
                        'Value': ‘February’
                    }
                ]
            }
        )
        return response
    except Exception as e:
        print(e)
        print('Error putting tag on object {} from bucket {}. '.format(key, bucket))
        raise e

