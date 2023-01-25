import subprocess
import os
import socket
import sys
import shutil
import time
import pytest
from cryptoadvance.specter.rpc import BitcoinRPC

@pytest.fixture(scope="session")
def start_spectrum(request):
    stop_service = False #  request.config.getoption("stop_service", default=False)
    if not is_port_in_use(8081):
        if os.path.exists('./data'):
            print("Deleted Data")
            shutil.rmtree('./data')
        print("Starting Spectrum!")
        with open('spectrum.log', 'w') as f:
            process = subprocess.Popen([sys.executable, '-m', 'cryptoadvance.spectrum', 'server', '--config', 'cryptoadvance.spectrum.config.EmzyElectrumLiteConfig'], stdout=f, stderr=f, close_fds=True)
            time.sleep(1)
    else:
        print("Spectrum already running!")
    yield
    if stop_service:
        print("terminating")
        #process.terminate()

@pytest.fixture(scope="session")
def spectrum_mainchain_rpc(start_spectrum):
    rpc = BitcoinRPC(port=8081)
    assert rpc.test_connection()
    return rpc

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0
