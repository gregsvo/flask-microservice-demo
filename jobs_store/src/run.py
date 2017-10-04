from faker import Faker
from flask import Flask, json, jsonify, request
import logging


app = Flask(__name__)
data = []
fake = Faker()


# GET list of all active jobs
@app.route('/jobs', methods=['GET'])
def all_orders():
    print("JOBS STORE GET REQUEST RECEIVED FOR /JOBS")
    return jsonify(data), 200


# DELETE a job (does not delete, just adds 'off' toggle)-
@app.route('/jobs/<string:job_id>', methods=['DELETE'])
def stop_job(job_id):
    import ipdb;
    ipdb.set_trace()
    payload = {job_id: 'OFF'}
    return jsonify(payload), 200


# PUT a job update replaces existing commands for job, if job_id exists-
@app.route('/jobs/<string:job_id>', methods=['PUT'])
def update_job(job_id):
    import ipdb;
    ipdb.set_trace()
    job_data = request.get_json()
    payload = {'status': 'UPDATED', 'current_job_data': job_data}
    return jsonify(payload), 200


# GET information on individual job
@app.route('/jobs/<string:job_id>', methods=['GET'])
def get_job(job_id):
    import ipdb;
    ipdb.set_trace()
    payload = request.get_json()
    return jsonify(payload), 200


# GET a list of jobs by author_id
@app.route('/jobs/author/<string:author_id>', methods=['GET'])
def get_job_from_author_id(author_id):
    import ipdb;
    ipdb.set_trace()
    payload = {author_id: {'jobs': ['one', 'two', 'three']}}
    return jsonify(payload), 200


if __name__ == '__main__':
    app.logger.setLevel(logging.INFO)
    # app.run(debug=True, host='0.0.0.0', port=5466) #localdev
    app.run(debug=True, host='0.0.0.0')
