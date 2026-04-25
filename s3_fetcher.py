import boto3

s3 = boto3.client('s3')

BUCKET = "your-bucket-name"
PREFIX = "friend-ec2-logs/"

def fetch_logs():
    response = s3.list_objects_v2(Bucket=BUCKET, Prefix=PREFIX)

    logs = []

    for obj in response.get('Contents', []):
        key = obj['Key']
        data = s3.get_object(Bucket=BUCKET, Key=key)
        logs.append(data['Body'].read().decode('utf-8'))

    return logs