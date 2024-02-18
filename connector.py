import paramiko
 
def create_sftp_client(host, port, username, password):
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)
 
    sftp_client = paramiko.SFTPClient.from_transport(transport)
 
    return sftp_client

def download_file_from_server(sftp_client, remote_file, local_file):
    sftp_client.get(remote_file, local_file)


sftp_client = create_sftp_client("iss-nas.synology.me", 50, "user-guest", "syn#OStis2019")
download_file_from_server(sftp_client, "ml_model/synology.pub", "synology.txt")
sftp_client.close()