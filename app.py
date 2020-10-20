from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/Registro')
def registro():
    return render_template('CrearCuenta.html')

@app.route('/Admin')
def admin():
    return render_template('InterfazAdmin.html')    
if  __name__ == "__main__":
    app.run(debug=True,port=5000)