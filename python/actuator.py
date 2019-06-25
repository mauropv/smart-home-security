import sys
import os
import json
from web3.auto import w3
from eth_account import Account
import traceback


from web3 import Web3,HTTPProvider

def load_rules(ownerAddress):
  rules = []
  with open('config.json', 'r') as f1:
          config = json.load(f1)

  wConn = Web3(HTTPProvider(config['rinkeby_link']))

  with open('sdbb_abi.json', 'r') as f1:
          sdbb_abi = json.load(f1)

  sdbb = wConn.eth.contract(address=Web3.toChecksumAddress('0x0cdd3217dcfb2bdb456f9219ea1d81219ac74d7e'),abi=sdbb_abi)


  rulesIds = sdbb.functions.getRulesByOwner(Web3.toChecksumAddress(ownerAddress)).call()

  for id in rulesIds:
      rules.append(sdbb.functions.rules(id).call())
      print(sdbb.functions.rules(id).call())
  return rules

def check_packet(rules):
    tv = input("Message to verify\r\n")
    json1 = json.loads(tv)
    senderAddress = w3.eth.account.recoverHash(w3.sha3(text=str(json1['message'])), vrs=(json1['v'],json1['r'],json1['s']));

    print(senderAddress)
    print(rules)
    for rule in rules:
        if(rule[0]==senderAddress and rule[1]==localAccount.address and rule[2] == json1['message']['actionToExecute']):
            print("Action Accepted")
        else:
            print("Action Refused")



#check if auth.json exists

localPassword = "Password"
ownerAddress = ""
localAccount = ""

if(os.path.exists('auth-a.json')==False):
    authenticationSet = {}
    #generate keys
    localAccount = w3.eth.account.create('seed')

    accountDump = w3.eth.account.encrypt(localAccount.privateKey, localPassword);

    authenticationSet['keystore'] = accountDump
    ownerAddress = input("Insert the owner address\r\n")
    while(w3.isAddress(ownerAddress)==False):
        ownerAddress = input("Address not valid. Insert the owner address\r\n")
    authenticationSet['ownerAddress']=ownerAddress
    with open('auth-a.json', 'w') as f:
            json.dump(authenticationSet, f)
else:
    with open('auth-a.json', 'r') as f:
        datastore = json.load(f)
    privateKey = w3.eth.account.decrypt(datastore['keystore'],localPassword)
    localAccount = w3.eth.account.privateKeyToAccount(privateKey);
    ownerAddress = datastore['ownerAddress']
print(localAccount.address)
rules = load_rules(ownerAddress)

while(True):
    try:
        check_packet(rules)
    except Exception:
        traceback.print_exc()

    rules = load_rules(ownerAddress)



