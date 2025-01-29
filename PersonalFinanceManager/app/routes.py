# app/routes.py

from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_user, current_user, login_required, logout_user
from app import db
from app.models import User, Transaction, Savings
import csv
from io import StringIO

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def home():
    return render_template('home.html')

@main.route('/report')
@login_required
def generate_report():
    transactions = Transaction.query.filter_by(user_id=current_user.id).all()
    
    # Create CSV data
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['Amount', 'Category', 'Date', 'Description'])
    
    for transaction in transactions:
        writer.writerow([transaction.amount, transaction.category, transaction.date, transaction.description])
    
    output.seek(0)
    return send_file(output, mimetype='text/csv', as_attachment=True, attachment_filename='transactions_report.csv')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))
