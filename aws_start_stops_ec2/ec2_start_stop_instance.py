import boto3

instance_id_1 = ''
instance_id_2 = ''
action = 'stop'

ec2_client = boto3.client('ec2', region_name='us-east-1')

def action_instance(action, instanceids):

  if action == 'start':
    response = ec2_client.start_instances(
      InstanceIds=instanceids
    )    
    for info in response['StartingInstances']:
      current_state = info['CurrentState']['Name']
      previous_state = info['PreviousState']['Name']
      print(f'Resultado: Status anterior: {previous_state} - Status atual: {current_state}')

  elif action == 'stop':

    response = ec2_client.stop_instances(
      InstanceIds=instanceids
    )
    for info in response['StoppingInstances']:
      current_state = info['CurrentState']['Name']
      previous_state = info['PreviousState']['Name']
      print(f'Resultado: Status anterior: {previous_state} - Status atual: {current_state}')
    # print(response)

  else:
    print('Ação não encontrada!')

action_instance(
  action=action, 
  instanceids=[instance_id_1]
)