from flask import render_template
from app import db
from app import models


def index():
    transactions = models.Transactions.query.all()
    return render_template('index.html', transactions=transactions)
