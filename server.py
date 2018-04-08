# -*- coding: utf-8 -*-
# !/usr/bin/env python
# __author__ = 'hongkefeng'

from __future__ import unicode_literals

import random

from flask import Flask
from flask.globals import request
from flask.json import jsonify

from flask import (Flask, render_template, redirect, url_for, request, flash)
from flask_bootstrap import Bootstrap
from ext import db
from models import TodoList

SECRET_KEY = 'key'

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:wdbuyer@10.1.101.161/wdbuyer_test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)


@app.route('/create/')
def test():
    params = request.args

    device_id = params.get("device_id")

    todo = TodoList(random.randint(10, 1000), params.get("title"), 1)
    todo.save()

    return jsonify({"test": todo.create_time})


def login_require(func):
    def decorator(*args, **kwargs):
        username = request.args.get('username')
        if username and username == 'admin':
            return func(*args, **kwargs)
        else:
            return redirect("login")

    return decorator


app.run(debug=True)
