from flask import Flask, json, jsonify, request
import logging
import requests


app = Flask(__name__)


# GET list of all active jobs - returns data from job_store
@app.route('/jobs', methods=['GET'])
def get_all_jobs():
    count = request.args.get('count')
    data = requests.get('http://steve_jobs_store:5000/jobs').json()
    if count:
        return jsonify(data[:int(count)]), 200
    else:
        return jsonify(data), 200


# GET an individual job data - forwards deletion request to job_store microservice
@app.route('/jobs/<string:job_id>', methods=['GET'])
def get_job(job_id):
    import ipdb;
    ipdb.set_trace()
    response = requests.get('http://localhost:5466/jobs/{}'.format(job_id)).json()
    return jsonify(response), 200


# GET a list of jobs for an author id - forwards request to job_store microservice
@app.route('/jobs/author/<string:author_id>', methods=['GET'])
def get_job_from_author_id(author_id):
    import ipdb;
    ipdb.set_trace()
    response = requests.get('http://localhost:5466/jobs/author/{}'.format(author_id)).json()
    return jsonify(response), 200


# POST a new job - forwards job to scheduler microservice
@app.route('/jobs', methods=['POST'])
def add_job():
    import ipdb;
    ipdb.set_trace()
    job_data = request.get_json()
    response = requests.post('http://localhost:5455/jobs', json=job_data).json()
    return jsonify(response), 200


# DELETE a job (does not delete, just adds 'off' togle)- forwards deletion request to job_store microservice
@app.route('/jobs/<string:job_id>', methods=['DELETE'])
def stop_job(job_id):
    import ipdb;
    ipdb.set_trace()
    response = requests.delete('http://localhost:5466/jobs/{}'.format(job_id)).json()
    return jsonify(response), 200


# PUT update to job - forwards update request to job_store microservice
@app.route('/jobs/<string:job_id>', methods=['PUT'])
def update_job(job_id):
    import ipdb;
    ipdb.set_trace()
    job_data = request.get_json()
    response = requests.put('http://localhost:5466/jobs/{}'.format(job_id), json=job_data).json()
    return jsonify(response), 200


if __name__ == '__main__':
    app.logger.setLevel(logging.INFO)
    # app.run(debug=True, host='0.0.0.0', port=5488) #localdev
    app.run(debug=True, host='0.0.0.0')
