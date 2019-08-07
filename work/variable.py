import boto3

# varible
tableName = 'vcloudlab_picture'
queueName = 'vcloudlab_sqs_queue'
bucketName = 'vcloudlab-bucket'

sqs_resource = boto3.resource('sqs')
sqs_client = boto3.client('sqs')
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

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