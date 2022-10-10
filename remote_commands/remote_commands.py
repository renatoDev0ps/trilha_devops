from sys import stderr, stdout
import paramiko

address = 'ip_from_server'
username = 'user from server'
password = 'password from server'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=address, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command()
stdin.close()
interface = []
for line in stdout.readlines():
  result = line.replace('\n','')
  if 'mtu' in line:
    interface_name = result.split(':')[0]
    interface.append(interface_name)
ssh.close()
print(interface)