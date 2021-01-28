import requests

url = "https://api.thegraph.com/subgraphs/name/cryptexglobal/tcap-rinkeby"
json = {'query': '{vaults(where: {collateral_lt:"205"}) { id vaultId owner collateral currentRatio }}'}
response = requests.post(url=url, json=json)

print(response.text)