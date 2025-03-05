"""
RCE-Vulnerable FTP server.

:author: Max Milazzo
"""


import os
from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer


class VulnerableFTPHandler(FTPHandler):
    """
    Custom FTP handler.
    """
    
    def on_file_sent(self, file):
        os.system("logger.bat GET " + file)
        
    
    def on_file_received(self, file):
        os.system("logger.bat PUT " + file)


def main():
    """
    Starts an FTP server with the vulnerable handler.
    """
    
    authorizer = DummyAuthorizer()
    authorizer.add_user("root", "password", "files", perm="elradfmw")

    handler = VulnerableFTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("0.0.0.0", 21), handler)
    server.serve_forever()


if __name__ == "__main__":
    main()