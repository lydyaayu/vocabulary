import requests

api_key = 'f8777afc-be1c-41a2-bb78-045e19a79f8e'
word = 'voluminous'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(final_url)
result = r.json()
print(result)