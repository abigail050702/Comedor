from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Datos predeterminados para simular el sistema sin base de datos
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # Datos predeterminados para las tarjetas y gráficas del Dashboard
    stats = {
        "atendidos": 250,
        "preparados": 500,
        "restantes": 250,
        "matutino": 150,
        "vespertino": 100
    }
    return render_template('dashboard.html', stats=stats)

@app.route('/alumnos')
def alumnos():
    # Lista predeterminada de alumnos
    lista_alumnos = [
        {"registro": 1, "matricula": "2023001", "nombre": "Juan Pérez", "turno": "Matutino", "platillos": 1},
        {"registro": 2, "matricula": "2023002", "nombre": "María Gómez", "turno": "Vespertino", "platillos": 1}
    ]
    return render_template('alumnos.html', alumnos=lista_alumnos)

@app.route('/platillos')
def platillos():
    lista_platillos = [
        {"turno": "Matutino", "fecha": "2026-09-28", "nombre": "Pechuga asada", "descripcion": "Incluye arroz y ensalada"}
    ]
    return render_template('platillos.html', platillos=lista_platillos)

@app.route('/turnos')
def turnos():
    return render_template('turnos.html')

@app.route('/reportes')
def reportes():
    reporte_consumo = [
        {"fecha": "2026-09-28", "matricula": "2023001", "nombre": "Juan Pérez", "turno": "Matutino", "operador": "Admin"}
    ]
    return render_template('reportes.html', reporte=reporte_consumo)

@app.route('/configuracion')
def configuracion():
    return render_template('configuracion.html')

if __name__ == '__main__':
    app.run(debug=True)   