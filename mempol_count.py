from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException


access = AuthServiceProxy("http://aliathanasoulas:aliathanasoulas@127.0.0.1:8332")
a = len(access.getrawmempool())
print a
