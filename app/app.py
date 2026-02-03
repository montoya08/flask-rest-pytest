from flask import Flask, jsonify, request  # Flask is imported to obtain the framework for creating the server
                                           # jsonify jsonify to convert data from Python to JSON
                                           # request to allow reading what it receives from Post or Put

app = Flask(__name__) # The Flask application is created

data = [] # Database simulation

@app.route('/') #Defines the server's root path
def home():
    return jsonify(data) # returns the data list in json format

# Get method
# The GET endpoint exposes the current state of the list and returns all items in JSON format
@app.route('/elements', methods=['GET']) 
def get():
    return jsonify(data) 

# Post method
# The POST endpoint receives an item in JSON format, adds it to the list, and returns the updated data status
@app.route('/elements', methods=['POST']) 
def post():
    element =  request.json.get('element')
    data.append(element)
    return jsonify({'data': data})

# Put method
# The PUT endpoint updates an existing item in the list, identified by its index in the URL, after first validating that the index is valid
@app.route('/elements/<int:index>', methods=['PUT']) 
def put(index):
    element = request.json.get('element')
    if 0 <= index < len (data):
        data[index] = element
        return jsonify({'data': data})
    return jsonify({'error': 'Index out of range'}), 404

# Delete method
# The DELETE endpoint removes a specific item from the list using its index, after first validating that it exists
@app.route('/elements/<int:index>', methods=['DELETE']) 
def delete(index):
    if 0 <= index < len (data):
        delete = data.pop(index)
        return jsonify({'element': delete, 'data': data})
    return jsonify({'error': 'Index out of range'}), 404


# This block ensures that the Flask server only runs when the file is executed directly
# Additionally, it explicitly defines the host and port to allow the application to be accessible from remote environments such as GitHub Codespaces
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)