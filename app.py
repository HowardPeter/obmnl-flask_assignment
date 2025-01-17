# Import libraries
from flask import Flask, url_for, request, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route('/')
def get_transactions():
    return render_template('transactions.html', transactions=transactions)

# Create operation
@app.route('/create', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        # Create a new transaction object using form field values
        transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
        }
        # Append the new transaction to the transactions list
        transactions.append(transaction)
        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for('get_transactions'))
        
    return render_template('form.html')

# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = request.form['date']
                transaction['amount'] = float(request.form['amount'])
                break
            
        return redirect(url_for('get_transactions'))
    
    # If the request method is GET, find the transaction with the matching ID and render the edit form
    if request.method == 'GET':
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                # Render the edit form template and pass the transaction to be edited
                return render_template('edit.html', transaction=transaction)
    
    return {"message": "Transaction not found"}, 404

# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction) # Remove the transaction from the transactions list
            break
        
    # Redirect to the transactions list page after deleting the transaction
    return redirect(url_for('get_transactions'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)