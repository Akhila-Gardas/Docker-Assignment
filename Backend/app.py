from flask import Flask, request

app = Flask(__name__)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    # Capture data parameters sent from the Express frontend form
    item_name = request.form.get('itemName')
    item_desc = request.form.get('itemDescription')
    
    return f"<h3>Data successfully captured by Flask Container!</h3><p>Item: {item_name}</p><p>Description: {item_desc}</p>"

if __name__ == '__main__':
    # Run server on port 5000, open to network paths
    app.run(host='0.0.0.0', port=5000)