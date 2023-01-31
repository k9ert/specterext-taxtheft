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
import time

logger = logging.getLogger(__name__)


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
        allow_threading_for_testing=False
    )
    

    logger.info("Creating wallet ...")
    wallet: Wallet = wm.create_wallet("wallet", 1, "wpkh", [device.keys[0]], [device])
    wallet.update_balance()
    time.sleep(1)
    
    logger.info(f"wallet.txlist length: {len(wallet.txlist())}")
    logger.info(f"utxo: {wallet.check_utxo()}")
    logger.info(f"addresses: {wallet.check_addresses()}")
    logger.info(f"addresses: {wallet.addresses}")
    assert False
