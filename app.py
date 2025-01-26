"""
Flask application for managing transactions.
This app demonstrates basic CRUD operations.
"""

from flask import Flask, url_for, request, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300},
]


@app.route('/')
def get_transactions():
    """Retrieve and display the list of transactions."""
    return render_template('transactions.html', transactions=transactions)


@app.route('/create', methods=['GET', 'POST'])
def add_transaction():
    """Add a new transaction."""
    if request.method == 'POST':
        transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': float(request.form['amount']),
        }
        transactions.append(transaction)
        return redirect(url_for('get_transactions'))
    return render_template('form.html')


@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    """Edit an existing transaction."""
    if request.method == 'POST':
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = request.form['date']
                transaction['amount'] = float(request.form['amount'])
                break
        return redirect(url_for('get_transactions'))

    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template('edit.html', transaction=transaction)

    return {"message": "Transaction not found"}, 404


@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    """Delete a transaction."""
    transactions[:] = [
        transaction for transaction in transactions
        if transaction['id'] != transaction_id
    ]
    return redirect(url_for('get_transactions'))


if __name__ == '__main__':
    app.run(debug=True)
