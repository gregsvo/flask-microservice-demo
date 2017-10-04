import datetime

from project import db


class Job(db.Model):
    __tablename__ = "jobs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    foo = db.Column(db.String(128), nullable=False)
    bar = db.Column(db.String(128), nullable=False)
    toggle = db.Column(db.Boolean(), default=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, foo, bar, toggle, created_at=datetime.datetime.utcnow()):
        self.foo = foo
        self.bar = bar
        self.toggle = toggle
        self.created_at = created_at
