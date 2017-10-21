import requests

def get_balance(wallets):
	return bitcoin_balance(wallets["bitcoin"])


def bitcoin_balance(address):
	res = requests.get("https://blockchain.info/balance?active=%s" % address).json()

	balance = res[self.address]["final_balance"]
	
	res = requests.get("https://blockchain.info/ticker").json()

	currency = res["RUB"]["buy"]
	return balance*currency