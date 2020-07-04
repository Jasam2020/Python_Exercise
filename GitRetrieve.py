import requests

response = requests.get('https://api.github.com/search/repositories?q=language:python')
data = response.json()
for d in sorted(data['items'], key=lambda x: x['forks'], reverse=True):

    print(f"{d['forks']} {d['name']} {d['description']}")