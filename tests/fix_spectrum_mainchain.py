import subprocess
import os
import socket
import sys
import pytest

@pytest.fixture(scope="session")
def start_service():
    if not is_port_in_use(8081):
        with open('spectrum.log', 'w') as f:
            subprocess.Popen([sys.executable, '-m', 'cryptoadvance.spectrum', 'server', '--config', 'cryptoadvance.spectrum.config.EmzyElectrumLiteConfig'], stdout=f, stderr=f, close_fds=True)
    yield
    # yield is used here so that the teardown can happen after the test

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0
