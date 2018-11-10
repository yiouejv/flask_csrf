#encoding: utf-8
from functools import wraps
from flask import session
from flask import redirect, url_for

def loginRequired(fn):
    def wrapper(*args, **kwargs):
        id = session.get('user_id')
        if id:
            return fn(*args, **kwargs)
        else:
            return redirect(url_for('icbc.login'))
    return wrapper


