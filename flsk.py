from flask import Flask, jsonify, request
import serial
import time

app = Flask(__name__)

# @app.route('/get_data', methods=['GET'])
# def get_data():
#     # Make a GET request to the external website or API
#     url = 'http://127.0.0.1:5500/main.html'  # Example URL (replace with the website/API you want)
#     response = requests.get(url)
    
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Return the data as a JSON response
#         return jsonify(response.json())
#     else:
#         return jsonify({"error": "Failed to retrieve data"}), 500
    
@app.route('/send-data', methods=['POST'])
def get_data():
    # Get JSON data from the request body
    input_data = request.form.get('input')
    print(input_data)
    
    if input_data:
        arduino = serial.Serial("COM9", 9600)
        arduino.write((input_data + "\n").encode())
        # Echo back the 'input' value
        return jsonify({"input": input_data})
    else:
        # Return an error message if 'input' is not provided
        return jsonify({"error": "'input' field not found in the form data"}), 400


if __name__ == '__main__':
    app.run(debug=True)