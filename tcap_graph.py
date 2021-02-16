import requests
import json

url = "https://api.thegraph.com/subgraphs/name/cryptexglobal/tcap-rinkeby"
json = {'query': '{vaults(where: {currentRatio_gt:"0", currentRatio_lt:"225"}) {vaultId owner debt collateral currentRatio address}}'}
response = requests.post(url=url, json=json)
_data = response.json()
vaults = []
if _data['data'] == []:
    print('No vaults with currentRatio under 225')
else:
    for n  in _data['data']['vaults']:
        vaults.append(int(n.get('vaultId')))

print(_data)
print(vaults)
