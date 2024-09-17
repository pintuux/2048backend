# from flask import Flask, jsonify
# from flask_cors import CORS
# import subprocess


# app = Flask(__name__)
# CORS(app)  # Enable cross-origin requests for communication with React

# @app.route('/')
# def home():
#     return jsonify(message="Server is running")
# @app.route('/start-game', methods=['GET'])
# def start_game():
#     try:
#         # Ensure the path to sudoku.py is correct
#         script_path = r'sudoku.py'

#         # Execute the script
#         result = subprocess.run(['python', script_path], capture_output=True, text=True)
#         # print(result)
#         output = result.stdout
#         # print(output)
#         return jsonify({'message': 'Game started', 'output': output})
#     except Exception as e:
#         return jsonify({'message': 'Error occurred', 'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify, request
import logicfinal
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Initialize the game
matrix = logicfinal.start_game()
logicfinal.add_new_2(matrix)
logicfinal.add_new_2(matrix)
@app.route('/')
def homepage():
    return jsonify("server is running")
@app.route('/start-game', methods=['GET'])
def start_game():
    global matrix
    matrix = logicfinal.start_game()
    logicfinal.add_new_2(matrix)
    logicfinal.add_new_2(matrix)
    return jsonify(matrix)

@app.route('/move', methods=['POST'])
def move():
    global matrix
    direction = request.json.get('direction')
    if direction == 'UP':
        matrix, _ = logicfinal.move_up(matrix)
    elif direction == 'DOWN':
        matrix, _ = logicfinal.move_down(matrix)
    elif direction == 'LEFT':
        matrix, _ = logicfinal.move_left(matrix)
    elif direction == 'RIGHT':
        matrix, _ = logicfinal.move_right(matrix)

    # Add a new tile if the board changed
    logicfinal.add_new_2(matrix)
    
    status = logicfinal.get_current_state(matrix)
    return jsonify({'matrix': matrix, 'status': status})

if __name__ == "__main__":
    app.run(debug=True)
