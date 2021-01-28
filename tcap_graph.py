import requests

url = "https://api.thegraph.com/subgraphs/name/cryptexglobal/tcap-rinkeby"
json = {'query': '{vaults(where: {currentRatio_lt:"205", currentRatio_gt:"0"}) { vaultId }}'}
response = requests.post(url=url, json=json)

print(response.text)