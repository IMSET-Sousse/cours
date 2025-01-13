from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = 'Maher'
    return f'Bonjour {name}'

@app.route('/date')
def date():
    return f'La date actuelle est {datetime.now()}'

@app.route('/info')
def info():
    name = 'Maher'
    age = 20
    return f'Je suis {name} et je suis {age} ans'

if __name__ == '__main__':
    app.run(debug=True)