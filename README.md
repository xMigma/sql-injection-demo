# Demostración de Inyección SQL con Flask y SQLite

Este proyecto es una aplicación web básica en Flask diseñada para demostrar los peligros de las inyecciones SQL. **No debe utilizarse en producción o con datos reales**. La aplicación permite que un usuario inicie sesión utilizando credenciales almacenadas en una base de datos SQLite. Sin embargo, la forma en que se construye la consulta SQL en esta aplicación la hace vulnerable a ataques de inyección SQL.

## Advertencia

**Este proyecto es intencionalmente inseguro y solo debe usarse para fines educativos.** No lo implementes en ningún entorno real. El objetivo es mostrar cómo las consultas SQL mal implementadas pueden ser manipuladas para ejecutar comandos no deseados.

## Requisitos

- Python 3.7 o superior
- Flask 2.3.2

## Instalación

1. Clona el repositorio o descarga los archivos.

2. Navega hasta el directorio del proyecto.

3. Instala las dependencias utilizando `pip`:

   ```bash
   pip install -r requirements.txt

## Uso

1. Inicializa la base de datos:

   La base de datos se inicializa automáticamente cuando se ejecuta la aplicación por primera vez. La función `init_db()` crea una tabla `usuarios` si no existe.

2. Ejecuta la aplicación:

   ```bash
   python app.py
   ```

3. Abre tu navegador y navega a `http://127.0.0.1:5000/` para acceder a la aplicación.

4. Intenta iniciar sesión utilizando las credenciales almacenadas en la base de datos o prueba con una inyección SQL básica como:

   ```plaintext
   usuario: ' OR '1'='1
   contraseña: ' OR '1'='1
   ```

   Esto debería permitirte iniciar sesión sin necesidad de conocer el nombre de usuario o la contraseña correctos, demostrando así la vulnerabilidad.

## Estructura del Proyecto

- `app.py`: El archivo principal que contiene la lógica de la aplicación Flask.
- `templates/`: Directorio que contiene los archivos HTML para las vistas.
  - `login.html`: Página de inicio de sesión.
  - `success.html`: Página mostrada al iniciar sesión con éxito.
- `usuarios.db`: Base de datos SQLite que almacena los nombres de usuario y contraseñas.

## Notas

- La aplicación está configurada para ejecutarse en modo de depuración (`debug=True`), lo cual es útil para desarrollo. No olvides desactivar este modo en un entorno de producción.
- **El código intencionalmente construye consultas SQL inseguras para fines educativos.** No se debe seguir este patrón en aplicaciones reales.
- Para protegerse contra inyecciones SQL, las consultas SQL deben parametrizarse, es decir, no concatenar directamente las entradas del usuario en las consultas.