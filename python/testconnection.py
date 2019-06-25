import sys
import os
import json
from web3.auto import w3
from eth_account import Account
from web3 import Web3,HTTPProvider

with open('config.json', 'r') as f1:
        config = json.load(f1)


wConn = Web3(HTTPProvider(config['rinkeby_link']))


with open('sdbb_abi.json', 'r') as f1:
        sdbb_abi = json.load(f1)

sdbb = wConn.eth.contract(address=Web3.toChecksumAddress('0x0cdd3217dcfb2bdb456f9219ea1d81219ac74d7e'),abi=sdbb_abi)

print(sdbb.functions.rules(0).call())

print(sdbb.functions.getRulesByOwner(Web3.toChecksumAddress('0x78cee39846bcfee639060d1db9a4456cfaf5eb9e')).call())