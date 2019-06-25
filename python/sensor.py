import sys
import os
import json
import time
import random

from web3.auto import w3


#check if auth.json exists
localPassword = "Password"
if(os.path.exists('auth-s.json')==False):
#case auth.json does not exist
    authenticationSet = {}
    #generate keys
    localAccount = w3.eth.account.create('seed')

    accountDump = w3.eth.account.encrypt(localAccount.privateKey, localPassword);

    authenticationSet['keystore'] = accountDump
    #ownerAddress = input("Insert the owner address\r\n")
    with open('auth-s.json', 'w') as f:
            json.dump(authenticationSet, f)
else:
#case it exists
    with open('auth-s.json', 'r') as f:
        datastore = json.load(f)
    privateKey = w3.eth.account.decrypt(datastore['keystore'],localPassword)
    localAccount = w3.eth.account.privateKeyToAccount(privateKey);

print(localAccount.address)


packetToSend = {}
packetToSend['actionToExecute'] = input("Insert the sensed information\r\n")
packetToSend['timestamp'] = int(time.time())
packetToSend['nonce'] = random.randint(9999,99999)

packet_string = str(packetToSend)
messageSHA3 = w3.sha3(text=packet_string)
signature = w3.eth.account.signHash(messageSHA3,localAccount.privateKey)

completePacket = {}

completePacket['message']=packetToSend
completePacket['v']=signature['v']
completePacket['r']=signature['r']
completePacket['s']=signature['s']

print(json.dumps(completePacket))


