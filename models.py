# -*- coding: UTF-8 -*-
# !/usr/bin/python

import time
from ext import db


class TodoList(db.Model):
    __tablename__ = 'todolist'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(1024), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, title, status):
        self.user_id = user_id
        self.title = title
        self.status = status
        self.create_time = time.time()

    def verify(self):
        pass

    def save(self):
        db.session.add(self)
        db.session.commit()


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), nullable=False)
    password = db.Column(db.String(24), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        db.session.add(self)
        db.session.commit(self)


class Task(db.Model):
    __tablename__ = "uia_task"
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(128), nullable=False)
    task_name = db.Column(db.String(128), nullable=False)
