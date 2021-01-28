import requests
import json

url = "https://api.thegraph.com/subgraphs/name/cryptexglobal/tcap-rinkeby"
json = {'query': '{vaults(where: {currentRatio_lt:"205", currentRatio_gt:"0"}) { vaultId }}'}
response = requests.post(url=url, json=json)
_data = response.json()
vaults = []
if _data['data'] == []:
    print('No vaults with currentRatio under 205')
else:
    for n  in _data['data']['vaults']:
        vaults.append(int(n.get('vaultId')))

print(vaults)
