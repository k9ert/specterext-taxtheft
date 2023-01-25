import pytest
import os
from cryptoadvance.specter.rpc import BitcoinRPC
from cryptoadvance.specter.managers.wallet_manager import WalletManager
from cryptoadvance.specter.managers.device_manager import DeviceManager
from cryptoadvance.specter.key import Key
from cryptoadvance.specter.device import Device
from cryptoadvance.specter.wallet import Wallet
import json
import logging


# Let spectrum run after the test is finished
def test_something(caplog, spectrum_mainchain_rpc, devices_filled_data_folder):
    caplog.set_level(logging.DEBUG)
    # start_spectrum is a fixture which we won't use
    # stop_service is a parameter which we won't use
    rpc: BitcoinRPC = spectrum_mainchain_rpc
    
    dm: DeviceManager = DeviceManager(os.path.join(devices_filled_data_folder, "devices"))
    with open("tests/test_data/device.json", "r") as f:
        device = Device.from_json(json.load(f), dm)

    wm: WalletManager = WalletManager(
        None,
        "tests/test_data",
        rpc,
        "main",
        dm,
    )
    if wm.failed_load_wallets:
        wm.create_wallet("wallet", 1, "wpkh", [device.keys[0]], [device])

    


    #wallet: Wallet = Wallet()
    
    wallet: Wallet = wm.wallets["specter/wallet_2"]
    
    print(wallet.txlist())
    assert False
