#encoding: utf-8
from flask import Blueprint, request, render_template

bp = Blueprint('viruses', __name__, url_prefix='/v')

@bp.route('/')
def index():
    return render_template('viruses/index.html')


@bp.route('/transfer/')
def transfer():
    return render_template('viruses/transfer.html')