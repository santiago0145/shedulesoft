from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "hello world"

@app.route('/insert',methods = ['POST'])
def insertar():
        flash('Te has registrado correctamente!')

        if request.method == "POST":
                nombre = request.form['nombre']
                correo = request.form['correo']
                nombre_usuario = request.form['nombre_usuario']
                contrasena = request.form['contrasena']
                conexion = mysql.connection.cursor()
                conexion.execute("INSERT INTO usuarios (nombres, correo, usuario, password) VALUES (%s, %s, %s,%s)", (nombre, correo, nombre_usuario, contrasena,))
                mysql.connection.commit()
                return redirect(url_for('login'))
#registro usuario
@app.route('/insert',methods = ['POST'])
def insertar():
        flash('Te has registrado correctamente!')

        if request.method == "POST":
                nombre = request.form['nombre']
                correo = request.form['correo']
                nombre_usuario = request.form['nombre_usuario']
                contrasena = request.form['contrasena']
                conexion = mysql.connection.cursor()
                conexion.execute("INSERT INTO usuarios (nombres, correo, usuario, password) VALUES (%s, %s, %s,%s)", (nombre, correo, nombre_usuario, contrasena,))
                mysql.connection.commit()
                return redirect(url_for('login'))
if __name__ == "__main__":
	app.run(debug=True)
