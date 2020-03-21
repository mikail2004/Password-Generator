import random
import os
from flask import Flask, render_template

app = Flask(__name__, template_folder='web', static_folder='static')

def generator():
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    num1 = random.randint(1000, 2000)
    num2 = random.randint(1500, 1600)
    letter1 = random.choice(alphabets)
    letter2 = random.choice(alphabets)
    password = letter1 + str(num1) + str(num2) + letter2
    return password
    
@app.route('/')
def index():
    return render_template('index.html', message=generator())

if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 5000))
    #app.run(debug=True, host='0.0.0.0', port=port)
    app.run()
