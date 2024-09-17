from flask import Flask, jsonify
from flask_cors import CORS
import subprocess


app = Flask(__name__)
CORS(app)  # Enable cross-origin requests for communication with React

@app.route('/', methods=['GET'])
def homePage():
    return jsonify("Server is running on port 5000")

@app.route('/start-game', methods=['GET'])
def start_game():
    try:
        # Ensure the path to sudoku.py is correct
        script_path = r'sudoku.py'

        # Execute the script
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        # print(result)
        output = result.stdout
        # print(output)
        return jsonify({'message': 'Game started', 'output': output})
    except Exception as e:
        return jsonify({'message': 'Error occurred', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
