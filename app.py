from flask import Flask
from flask import render_template
from flask_cors import CORS
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
    app.run(debug=True,port=5000)