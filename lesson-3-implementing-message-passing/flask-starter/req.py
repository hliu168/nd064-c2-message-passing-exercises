import requests

URL = 'http://localhost:5000/api/orders/computers'

r = requests.get(URL)
if r.status_code == 200:
	print(type(r.json()))
	print(r.json())

body = {
	'created_by': 'robert.liu',
	'status': 'PROCESSING',
	'created_at': '2020-10-16T10:31:10.969696',
	'equipment': [
		'PC'
	]
}

r = requests.post(URL, json = body)
if r.status_code == 200:
	print(type(r.json()))
	print(r.json())
