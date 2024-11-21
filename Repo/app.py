from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        precio_tarro = 9000
        total_sin_descuento = tarros * precio_tarro

        # Aplicación de descuento
        if 18 <= edad <= 30:
            descuento = 0.15  # 15% de descuento
        elif edad > 30:
            descuento = 0.25  # 25% de descuento
        else:
            descuento = 0  # Sin descuento

        # Calcular el monto del descuento
        monto_descuento = total_sin_descuento * descuento

        # Calcular el total con descuento
        total_con_descuento = total_sin_descuento - monto_descuento

        # Convertir monto_descuento a entero
        monto_descuento = int(monto_descuento)

        # Convertir total_con_descuento a entero
        total_con_descuento = int(total_con_descuento)

        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                               total_con_descuento=total_con_descuento, monto_descuento=monto_descuento, resultado=True)


    return render_template('ejercicio1.html', resultado=False)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario == 'Juan' and contrasena == 'admin':
            mensaje = f'Bienvenido administrador {usuario}'
        elif usuario == 'Pepe' and contrasena == 'user':
            mensaje = f'Bienvenido usuario {usuario}'
        else:
            mensaje = 'Usuario o contraseña incorrectos.'

        return render_template('ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)