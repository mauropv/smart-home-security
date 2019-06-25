from web3.auto import w3
import json;
import base64;

acct = w3.eth.account.create('ACCOUNT1')


priKey = acct.privateKey



acct2 = w3.eth.account.privateKeyToAccount(priKey);


msgDict = {}
msgDict['src']="src"
msgDict['dst']="dst"
msgDict['sct']="act"

message = w3.sha3(text=str(msgDict))

signatureZ = w3.eth.account.signHash(message,acct.privateKey)

print(message)
sing= signatureZ['signature'].decode("ISO-8859-1")

senderAddress = w3.eth.account.recoverHash(message, signature=sing.encode("ISO-8859-1"));

print(acct2.address)
print(senderAddress)


print(signatureZ)

r = signatureZ['r']
s = signatureZ['s']
v = signatureZ['v']

msg = {}
msg['a'] = str(msgDict)
msg['r'] = r
msg['s'] = s
msg['v'] = v

jsn_string = json.dumps(msg)
print(jsn_string)


json1 = json.loads(jsn_string)
print (json1)

senderAddress = w3.eth.account.recoverHash(w3.sha3(text=json1['a']), vrs=(json1['v'],json1['r'],json1['s']));
print(senderAddress)
