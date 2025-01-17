from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

from knn import useKnn as KNN

# Configuración de Flask
app = Flask(__name__)

# Configuración de la base de datos
DB_CONFIG = {
    'dbname': 'ecommerce',
    'user': 'postgres',
    'password': 'n0m3l0',
    'host': 'localhost',
    'port': '5432'
}

# Ruta para consultar todos los productos del banner
@app.route('/api/banner', methods=['GET'])
def get_data_banner():
    try:
        # Conexión a la base de datos
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        # Consulta SQL
        query = "SELECT * FROM productBanner;"
        cursor.execute(query)
        result = cursor.fetchall()

        # Cerrar la conexión
        cursor.close()
        connection.close()

        return jsonify(result), 200
    except Exception as e:
        # Imprime el error en la consola para depuración
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500
    
# Ruta para consultar todos los productos
@app.route('/api/productos', methods=['GET'])
def get_data():
    try:
        # Conexión a la base de datos
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        # Consulta SQL
        query = "SELECT * FROM products ORDER BY RANDOM() LIMIT 35;"
        cursor.execute(query)
        result = cursor.fetchall()

        # Cerrar la conexión
        cursor.close()
        connection.close()

        return jsonify(result), 200
    except Exception as e:
        # Imprime el error en la consola para depuración
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500
    
    # Ruta para consultar un producto por su ID
@app.route('/api/productos/<producto_id>', methods=['GET'])
def get_producto(producto_id):
    try:
        # Conexión a la base de datos
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        # Consulta SQL
        query = "SELECT * FROM products WHERE id = %s;"
        cursor.execute(query, (producto_id,))
        result = cursor.fetchone()
        # Cerrar la conexión
        cursor.close()
        connection.close()
        if result:
            return jsonify(result), 200
        else:
            return jsonify({'error': 'Producto no encontrado'}), 404
    except Exception as e:
        # Imprime el error en la consola para depuración
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500


    # Ruta para consultar productos similares
@app.route('/api/productos/similares/<producto_id>', methods=['GET'])
def get_producto_similar(producto_id):
    try:
        # Conexión a la base de datos
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        resultado = KNN(producto_id);
        # Consulta SQL
        query = "SELECT * FROM products ORDER BY RANDOM() LIMIT 35;" #WHERE id = %s;"
        cursor.execute(query)#, (producto_id,))
        result = cursor.fetchall()#fetchone()
        # Cerrar la conexión
        cursor.close()
        connection.close()
        if result:
            return jsonify(resultado), 200
        else:
            return jsonify({'error': 'Producto no encontrado'}), 404
    except Exception as e:
        # Imprime el error en la consola para depuración
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500













if __name__ == '__main__':
    app.run(debug=True)
