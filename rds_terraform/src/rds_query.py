from dotenv import load_dotenv

import os
import json
import pymysql

config = load_dotenv(".env")

endpoint = os.getenv("ENDPOINT")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
db_name = os.getenv("DB_NAME")

connection = pymysql.connect(host=endpoint, user=username, password=password, db=db_name)

def lambda_handler(event, context):
  
  cursor = connection.cursor()
  cursor.execute('SELECT user.id, user.email, user.username, role.id AS role_id, role.name AS role_name FROM user JOIN user_roles on (user.id=user_roles.user_id) JOIN role on (role.id=user_roles.role_id)')
  
  rows = cursor.fetchall()
  
  return {
    'statusCode': 200,
    'body': json.dumps(rows)
  }