from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from flask import Flask, jsonify, request
from flask_apscheduler import APScheduler
import logging
import requests


app = Flask(__name__)


@app.route('/jobs', methods=['POST'])
def add_job():
    import ipdb;
    ipdb.set_trace()
    job_data = request.get_json()
    return jsonify(job_data), 200


def job1(a, b):
    print(str(a) + ' ' + str(b))


class Config(object):
    JOBS = [{'id': 'job1',
             'func': job1,
             'args': (1, 2),
             'trigger': 'interval',
             'seconds': 10}]

    # SCHEDULER_JOBSTORES = {'default': SQLAlchemyJobStore(url='sqlite://')}

    SCHEDULER_EXECUTORS = {'default': {'type': 'threadpool', 'max_workers': 20}}

    SCHEDULER_JOB_DEFAULTS = {'coalesce': False, 'max_instances': 3}

    SCHEDULER_API_ENABLED = True


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config())

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    # app.logger.setLevel(logging.INFO)
    app.run(debug=True, host='0.0.0.0', port=5455)
    # app.run(debug=True, host='0.0.0.0')
