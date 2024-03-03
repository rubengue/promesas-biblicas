import openpyxl
import random
from flask import Flask, appcontext_popped, jsonify, send_file
import os
from flask_cors import CORS

app = Flask(__name__)

# Load Bible verses and corresponding images from the Excel file
excel_file_path = './promesas-biblicas.xlsx'
image_folder_path = './imagenes'
workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook.active
data = [(cell.value, cell.offset(column=1).value, cell.offset(column=2).value, cell.offset(column=3).value) for cell in sheet['A'] if cell.value]  # Assuming verses are in column A, and images are in column B

@app.route('/api/random-verse', methods=['GET'])
def get_random_verse():
    random_entry = random.choice(data)
    texto = random_entry[0]
    verso = random_entry[2]
    image_file = random.choice(os.listdir(image_folder_path))
    image_path = 'https://picsum.photos/600'
    #image_path = os.path.join(image_folder_path, image_file)

    response = {'texto': texto, 'image_path': image_path, 'verso': verso}
    return jsonify(response)

@app.route('/api/verse-image', methods=['GET'])
def get_verse_image():
    image_path = request.args.get('url')
    return send_file(image_path, mimetype='image/jpg')  # Assuming images are in JPEG format

if __name__ == '__main__':
    app.run(debug=True)
