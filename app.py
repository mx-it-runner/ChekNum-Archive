from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()



# приложение работает и 
# слушает на http://127.0.0.1:5000/

# Теперь вы можете открыть ваш веб-браузер
# и перейти по адресу http://127.0.0.1:5000/