import json
import boto3
import uuid

s3 = boto3.client('s3')
ddb = boto3.resource('dynamodb')

def lambda_handler(event, context):
  table = ddb.Table("tabela")
  
  states_input = json.dumps(event)
  get_bucket_values = json.loads(states_input)
  
  try:
    
    bucket = get_bucket_values["detail"]["requestParameters"]["bucketName"]
    key = get_bucket_values["detail"]["requestParameters"]["key"]
    
    obj = s3.get_object(Bucket=bucket, Key=key)
    newData = {
      'id': str(uuid.uuid4().hex),
      'bucket': bucket,
      'filename': key,
      'filesize': int(obj['ContentLength']),
      'contentType': obj['ContentType'],
      'labelData': {},
      'faceData': {},
    }
    
    table.put_item(Item=newData)
    
    return newData
  
  except Exception as e:
    
    raise e