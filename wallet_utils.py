import requests

def get_balance(wallets):
	return bitcoin_balance(wallets["bitcoin"])


def bitcoin_balance(address):
	try:
		res = requests.get("https://blockchain.info/balance?active=%s" % address).json()

		balance = res[address]["final_balance"]
		
		res = requests.get("https://blockchain.info/ticker").json()

		currency = res["RUB"]["buy"]
		return round(balance*currency/10**8,2)
	except Exception:
		return 0