import simplejson
import json 

re = {}
re['data'] = []  

access = AuthServiceProxy("http://username:password@127.0.0.1:8332")
a = access.getrawmempool()

for tx in a:
    raw = access.getrawtransaction(tx)
    decoded = access.decoderawtransaction(raw)
    tx = decoded["hash"]
    amount = decoded["vout"][0]["value"]
    re['data'].append({'tx': tx, 'amount': amount})
   

print simplejson.dumps(re) 
