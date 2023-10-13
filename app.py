import pandas as pd
import openpyxl
from flask import Flask, render_template, url_for, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/number')
def cheknumber():
    return render_template("number.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'Файл не найден.', 400

        file = request.files['file']

        if file.filename == '':
            return 'Файл не выбран.', 400

        file.save(file.filename)
        return 'Файл успешно загружен.', 200
    else:
        return 'Для загрузки файлов разрешен только метод POST.'

if __name__ == '__main__':
    app.run(debug=True)