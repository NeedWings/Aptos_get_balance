from aptos_sdk.client import RestClient


f = open("addrs.txt", "r")
addrs = f.read().split("\n")
f.close()

APTOS_RPC = "https://fullnode.mainnet.aptoslabs.com/v1"

rest_client = RestClient(APTOS_RPC)

for addr in addrs:
	try:
		print("addr: " + addr + "   ---   " + str(int(rest_client.account_balance(addr))/100000000))
	except:
		print("addr: " + addr + "   ---    0")