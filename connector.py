import logging
import os
from io import StringIO

import paramiko
from dotenv import load_dotenv


class SFTPManager:
    def __init__(self, host: str, port: int, username: str, key_path: str):
        self.host = host
        self.port = port
        self.username = username
        self.key_path = key_path
        self.transport = None
        self.sftp_client = None

    def connect(self):
        key_data = self.load_private_key()
        key_file = paramiko.RSAKey.from_private_key(StringIO(key_data))
        self.transport = paramiko.Transport((self.host, self.port))
        self.transport.connect(username=self.username, pkey=key_file)
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

    def load_private_key(self):
        with open(self.key_path, encoding="utf-8") as f:
            return f.read()


def main():
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    sftp_user = os.environ["sftp-user"]
    sftp_key = os.environ["sftp-key"]
    sftp_host = os.environ["sftp-host"]
    sftp_port = int(os.environ["sftp-port"])
    local_file_path = (
        "model.pt"
    )
    if not all([sftp_user, sftp_key, sftp_host]):
        logging.error("SFTP credentials are not provided.")
        return

    sftp_manager = SFTPManager(sftp_host, sftp_port, sftp_user, sftp_key)
    try:
        sftp_manager.connect()
        logging.info("Connected to SFTP server.")
        sftp_manager.download_file("ml_model/model.pt", local_file_path)
        logging.info("File downloaded successfully.")
    except FileNotFoundError:
        logging.error("File not found on remote server.")
    except paramiko.SSHException as ssh_error:
        logging.error(f"SSH Error: {ssh_error}")
    finally:
        sftp_manager.close()


if __name__ == "__main__":
    main()
