import paramiko
import os 

SFTP_USER = os.environ["SFTP_USER"] 
SFTP_PASS = os.environ["SFTP_PASS"]
SFTP_HOST = os.environ["SFTP_HOST"]
SFTP_PORT = os.environ["SFTP_PORT"]

print(SFTP_HOST)
# def create_sftp_client(host, port, username, password):
#     transport = paramiko.Transport((host, port))
#     transport.connect(username=username, password=password)
 
#     sftp_client = paramiko.SFTPClient.from_transport(transport)
 
#     return sftp_client

# def download_file_from_server(sftp_client, remote_file, local_file):
#     sftp_client.get(remote_file, local_file)


# sftp_client = create_sftp_client(SFTP_HOST, SFTP_PORT, SFTP_USER, SFTP_PASS)
# download_file_from_server(sftp_client, "ml_model/synology.pub", "synology.txt")
# sftp_client.close()