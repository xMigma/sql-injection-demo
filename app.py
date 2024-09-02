from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        usuario TEXT NOT NULL,
        contraseña TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        conn = sqlite3.connect('usuarios.db', isolation_level=None)
        cursor = conn.cursor()

        query = f"SELECT usuario FROM usuarios WHERE usuario = '{usuario}' AND contraseña = '{contraseña}'"
        print(f"Ejecutando consulta: {query}")

        try:
            cursor.execute(query)
            usuario_db = cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error en la consulta SQL: {e}")
            error = f'Error en la consulta SQL: {e}'
            usuario_db = None

        conn.close()

        if usuario_db:
            return render_template('success.html', usuario=usuario_db[0], query=query)
        else:
            if not error:
                error = 'El nombre de usuario o la contraseña son incorrectos. Por favor, inténtelo de nuevo.'

    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
