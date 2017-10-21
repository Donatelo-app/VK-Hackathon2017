import requests
import os

def get_balance(wallets):
	return bitcoin_balance(wallets.get("bitcoin")) + tinkoff_balance(wallets.get("tinkoff"))


def bitcoin_balance(address):
	if not address: return 0 

	try:
		res = requests.get("https://blockchain.info/balance?active=%s" % address).json()

		balance = res[address]["final_balance"]
		device_id
		res = requests.get("https://blockchain.info/ticker").json()

		currency = res["RUB"]["buy"]
		return round(balance*currency/10**8,2)
	except Exception:
		return 0


def tinkoff_balance(inn):
	if not inn: return 0 

	token = os.environ.get("TINKOFF")
	device_id = os.environ.get("DEVICEID")

	if not token: return 0

	data = {"grant_type": "refresh_token",
			"refresh_token": token,
			"device_id": device_id}

	response = requests.post("https://openapi.tinkoff.ru/sso/secure/token", data=data).json()

	if not "access_token" in response: return 0

	response2 = requests.get("https://openapi.tinkoff.ru/sme/api/v1/partner/company/%s/accounts" % inn, headers={"Authorization": 'Bearer %s' % response["access_token"]}).json()

	return response2[0]["balance"]["otb"]