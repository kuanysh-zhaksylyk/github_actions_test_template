import paramiko
import os 

SFTP_USER = os.environ["sftp-user"] 
SFTP_PASS = os.environ["sftp-pass"]
SFTP_HOST = os.environ["sftp-host"]

SFTP_USER = os.environ.get("sftp-user")
if SFTP_USER is None:
    print("Variable 'sftp-user' is not set.")
    # Обработка ошибки или завершение скрипта

def create_sftp_client(host, port, username, password):
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)
 
    sftp_client = paramiko.SFTPClient.from_transport(transport)
 
    return sftp_client

def download_file_from_server(sftp_client, remote_file, local_file):
    sftp_client.get(remote_file, local_file)


sftp_client = create_sftp_client(SFTP_HOST, 50, SFTP_USER, SFTP_PASS)
download_file_from_server(sftp_client, "ml_model/synology.pub", "synology.txt")
sftp_client.close()