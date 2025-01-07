import os
import json
import psycopg2
from psycopg2 import sql
import lorem
import random
# Configuración de la conexión a la base de datos
DB_CONFIG = {
    "dbname": "ecommerce",
    "user": "postgres",
    "password": "n0m3l0",
    "host": "localhost",  # Cambiar si tu base de datos está en otro host
    "port": 5432,         # Cambiar si usas otro puerto
}

# Ruta de la carpeta donde están los archivos JSON
JSON_FOLDER = "C:/Users/tmarl/Documents/Escuela/Escom/6to/ai/proyecto/scrapping/buscados"

# Función para validar los datos
def validate_data(data):
    required_keys = ["title", "price", "rating", "link", "category", "image"]
    for key in required_keys:
        if not data.get(key):  # Checar si el valor está vacío o es None
            return False
    return True

def clean_price(value):
    """
    Limpia y convierte un valor de precio en formato string a float.
    """
    try:
        # Remover caracteres no deseados como '\n', '..', y espacios
        cleaned_value = value.replace("\n", "").replace("..", "").replace(",", "").replace("$", "").strip()
        return float(cleaned_value)
    except Exception as e:
        print(f"Error al limpiar el precio: {value} -> {e}")
        return None


def truncate(value, max_length):
    """
    Trunca un valor si excede la longitud máxima permitida.
    """
    return value[:max_length] if len(value) > max_length else value

# Función para transformar y limpiar datos
def transform_data(data):
    return {
        "name": truncate(data["title"], 400),  # Truncar a 400 caracteres
        "price": clean_price(data["price"]),
        "rating": float(data["rating"].split(' ')[0]),  # Tomar solo el primer número
        "image": truncate(data["image"], 400),  # Truncar a 400 caracteres
        "category": truncate(data["category"], 100),  # Truncar a 100 caracteres
        "url": truncate(data["link"], 400),  # Truncar a 400 caracteres
        "details": truncate(lorem.sentence(), 400),  # Truncar a 400 caracteres
        "quantity": random.randint(1, 1000),
    }



# Función principal
def load_json_to_db():
    try:
        # Conectar a la base de datos
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        print("Conexión a la base de datos exitosa.")
        
        # Procesar cada archivo JSON en la carpeta
        for file_name in os.listdir(JSON_FOLDER):
            if file_name.endswith(".json"):
                file_path = os.path.join(JSON_FOLDER, file_name)
                
                with open(file_path, "r", encoding="utf-8") as json_file:
                    try:
                        data = json.load(json_file)
                        
                        # Si los datos son una lista, procesar cada elemento
                        items = data if isinstance(data, list) else [data]
                        for item in items:
                            if validate_data(item):
                                transformed_data = transform_data(item)
                                
                                # Insertar en la base de datos
                                insert_query = sql.SQL("""
                                    INSERT INTO products (name, price, rating, image, category, url, details, quantity)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                """)
                                cursor.execute(insert_query, (
                                    transformed_data["name"],
                                    transformed_data["price"],
                                    transformed_data["rating"],
                                    transformed_data["image"],
                                    transformed_data["category"],
                                    transformed_data["url"],
                                    transformed_data["details"],
                                    transformed_data["quantity"]
                                ))
                                conn.commit()
                                print(f"Datos insertados desde: {file_name}")
                            else:
                                print(f"Datos inválidos en {file_name}: {item}")
                    except Exception as e:
                        print(f"Error al procesar el archivo {file_name}: {e}")
        
        # Cerrar la conexión
        cursor.close()
        conn.close()
        print("Conexión cerrada.")
    
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
if __name__ == "__main__":
    load_json_to_db()
