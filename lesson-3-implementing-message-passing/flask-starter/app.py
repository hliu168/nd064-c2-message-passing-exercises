import json
from flask import Flask, jsonify, request

from services import retrieve_orders, create_order

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})

@app.route('/api/orders/computers', methods=['GET', 'POST'])
def computers():
	if request.method == 'GET':
		return jsonify(retrieve_orders())
	elif request.method == 'POST':
		print(request)
		print(request.json)
		return jsonify(create_order(request.json))
	else:
		raise Exception('Unsupported method')	

if __name__ == '__main__':
    app.run()
