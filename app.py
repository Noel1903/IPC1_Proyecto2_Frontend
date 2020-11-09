from flask import Flask
from flask import render_template
from flask_cors import CORS
import os
app=Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/Login')
def login():
    return render_template('Login.html')  

@app.route('/Registro')
def registro():
    return render_template('CrearCuenta.html')

@app.route('/Admin')
def admin():
    return render_template('InterfazAdmin.html')  

@app.route('/Cliente')
def cliente():
    return render_template('InterfazClient.html')  

if  __name__ == "__main__":
    puerto=int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=puerto)
    