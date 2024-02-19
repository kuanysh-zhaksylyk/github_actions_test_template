import logging
import os

import paramiko


class SFTPManager:
    def __init__(self, host: str, port: int, username: str, password: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.transport = None
        self.sftp_client = None

    def connect(self):
        self.transport = paramiko.Transport((self.host, self.port))
        self.transport.connect(username=self.username, password=self.password)
        self.sftp_client = paramiko.SFTPClient.from_transport(self.transport)

    def close(self):
        if self.sftp_client:
            self.sftp_client.close()
        if self.transport:
            self.transport.close()

    def download_file(self, remote_file: str, local_file: str):
        if not self.sftp_client:
            raise ValueError("SFTP client is not connected.")
        self.sftp_client.get(remote_file, local_file)


def main():
    logging.basicConfig(level=logging.INFO)
    sftp_user = 'user-guest'
    sftp_pass = 'syn#OStis2019'
    sftp_host = 'iss-nas.synology.me'
    sftp_port = 50
    local_file_path = (
        "model.pt"
    )
    if not all([sftp_user, sftp_pass, sftp_host]):
        logging.error("SFTP credentials are not provided.")
        return

    sftp_manager = SFTPManager(sftp_host, sftp_port, sftp_user, sftp_pass)
    try:
        sftp_manager.connect()
        logging.info("Connected to SFTP server.")
        sftp_manager.download_file("ml_model/model.pt", local_file_path)
        logging.info("File downloaded successfully.")
    except FileNotFoundError:
        logging.error("File not found on remote server.")
    finally:
        sftp_manager.close()


if __name__ == "__main__":
    main()
