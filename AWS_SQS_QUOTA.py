import boto3
from botocore.exceptions import ClientError

def check_sqs_queue_status(access_key, secret_key, region, queue_url):
    try:
        # Initialize the SQS client
        sqs = boto3.client(
            'sqs',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )

        # Retrieve attributes of the specific queue
        response = sqs.get_queue_attributes(
            QueueUrl=queue_url,
            AttributeNames=[
                'ApproximateNumberOfMessages',
                'MaximumMessageSize',
                'MessageRetentionPeriod',
                'VisibilityTimeout'
            ]
        )

        attributes = response.get('Attributes', {})
        
        print(f"--- Statistics for Queue: {queue_url} ---")
        print(f"Messages currently in queue: {attributes.get('ApproximateNumberOfMessages')}")
        print(f"Max message size: {attributes.get('MaximumMessageSize')} bytes")
        print(f"Retention period: {attributes.get('MessageRetentionPeriod')} seconds")
        print(f"Visibility timeout: {attributes.get('VisibilityTimeout')} seconds")

    except ClientError as e:
        print(f"An error occurred: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Usage
if __name__ == "__main__":
    ACCESS_KEY = 'YOUR_ACCESS_KEY'
    SECRET_KEY = 'YOUR_SECRET_KEY'
    REGION = 'us-east-1'
    QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/123456789012/MyQueue'

    check_sqs_queue_status(ACCESS_KEY, SECRET_KEY, REGION, QUEUE_URL)
