import boto3
def lambda_handler(event, context):
    file_name = event['Records'][0]['s3']['object']['key'];
    service_name='s3'
    region_name='ap-south-1'
    aws_access_key_id='AKIATIRE3MO3ZYYUK23C'
    aws_secret_access_key='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'
    s3 = boto3.resource(
        service_name=service_name,
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
        )
    copy_source = {
        'Bucket': 'input-bucket-source-a',
        'Key': file_name
    }
    s3.meta.client.copy(copy_source, 'input-bucket-b',file_name)