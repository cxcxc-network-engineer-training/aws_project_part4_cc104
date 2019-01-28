import boto3

# varible
tableName = 'vcloudlab_picture'
bucketName = 'vcloudlab_bucket'
queueName = 'vcloudlab_sqs_queue'

s3_endpoint_url = 'http://s3.vcloudlab.pro:4569'
sqs_endpoint_url = 'http://sqs.vcloudlab.pro:9324'
dynamoDB_endpoint_url = 'http://dynamodb.vcloudlab.pro:8000'

baseURL = "http://s3.vcloudlab.pro:4569/s3/vcloudlab_bucket/"

s3_client = boto3.client(
    's3',
    endpoint_url = s3_endpoint_url)
s3_resource = boto3.resource(
    's3',
    endpoint_url = s3_endpoint_url)

sqs_client = boto3.client(
    'sqs',
    endpoint_url = sqs_endpoint_url)
sqs_resource = boto3.resource(
    'sqs',
    endpoint_url = sqs_endpoint_url)

dynamoDB_client = boto3.client(
    'dynamodb',
    endpoint_url = dynamoDB_endpoint_url)
dynamoDB_resource = boto3.resource(
    'dynamodb',
    endpoint_url = dynamoDB_endpoint_url)

# function
def send_message(filename):
    
    # 調用 SQS
    vlabQueues = sqs_client.list_queues( QueueNamePrefix = queueName )
    queue_url = vlabQueues['QueueUrls'][0]
    # print(queue_url)
    
    # 將 filename 透過 SQS 傳輸
    enqueue_response = sqs_client.send_message(
        QueueUrl = queue_url, 
        MessageBody = filename
    )
    # print('Message ID : ',enqueue_response['MessageId'])
    return True
    