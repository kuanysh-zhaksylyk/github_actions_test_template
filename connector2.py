import paramiko
from io import StringIO

host, port = 'iss-nas.synology.me',50
transport = paramiko.Transport((host, port))
username = 'user-guest'
key = '/home/kuanysh/.ssh/synology-key'

with open(key) as f:
    fin = f.read()
   
final_key=StringIO(fin)
keyFile=paramiko.RSAKey.from_private_key(final_key)
print(keyFile)
print(final_key)
transport = paramiko.Transport((host,port))
transport.connect(username=username,pkey=keyFile)

sftp = paramiko.SFTPClient.from_transport(transport)

sftp.get('ml_model/model.pt', 'test.pt')