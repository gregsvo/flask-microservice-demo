from faker import Faker
from flask import Flask, jsonify, request
import logging
import random


app = Flask(__name__)
data = []
fake = Faker()


@app.route('/create', methods=['PUT'])
def add_job():
    job_data = request.get_json()
    if not job_data:
        response_object = {'status': 'fail', 'message': 'Invalid job creation payload.'}
        return jsonify(response_object), 400


@app.route('/order/<int:num>', methods=['GET'])
def get_order(num):
    return jsonify(data[num]), 200


@app.route('/custSearch', methods=['POST'])
def cust_search():
    json = request.get_json()
    name = json.get('name', '')
    result = [order for order in data if name in order['cust']]
    return jsonify(result), 200


def create_order(num):
    return {'id': num,
            'cust': fake.name(),
            'items': [random.randint(1, 100) for _ in range(1, random.randint(1, 10))]}


def create_data():
    return [create_order(num) for num in range(1, 1000)]


if __name__ == '__main__':
    data = create_data()
    app.logger.setLevel(logging.INFO)
    # app.run(debug=True, host='0.0.0.0', port=5477) # localdev
    app.run(debug=True, host='0.0.0.0')
