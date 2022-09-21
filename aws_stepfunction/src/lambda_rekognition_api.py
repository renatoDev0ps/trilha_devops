from urllib import response
import boto3
import json
from decimal import Decimal

rekognition = boto3.client('rekognition')
s3 = boto3.client('s3')
ddb = boto3.resouce('dynamodb')

def detect_faces(bucket, key):
  response = rekognition.detect_faces(Image={"S3Object": { "Bucket": bucket, "Name": key}})
  return response

def detect_labels(bucket, key):
  response = rekognition.detect_labels(Image={"S3Object": { "Bucket": bucket, "Name": key }})
  return response

def lambda_handler(event, context):
  
  table = ddb.Table("tabela")
  
  states_input = json.dumps(event)
  get_input = json.loads(states_input)
  bucket = get_input["detail"]["requestParameters"]["bucketName"]
  key = get_input["detail"]["requestParameters"]["key"]
  
  try:
    
    face_detect = detect_faces(bucket, key)
    faces_map = json.loads(json.dumps(face_detect), parse_float=Decimal)
    
    label_detect = detect_labels(bucket, key)
    labels_map = json.loads(json.dumps(label_detect), parse_float=Decimal)
    
    table.update_item(
      key = {
        'filename': key,
      },
      UpdateExpression='set labelData = :label, faceData = :face',
      ExpressionAttributeValues={
        ':label': labels_map,
        ':face': faces_map
      },
      ReturnValues="UPDATE_NEW"
    )
    
    return faces_map

  except Exception as e:
    print(e)
    raise e