import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.neighbors import NearestNeighbors
import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    'dbname': 'ecommerce',
    'user': 'postgres',
    'password': 'n0m3l0',
    'host': 'localhost',
    'port': '5432'
}


def getProducts(ID_PRODUCTO):
    try:
        connection  = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        query  = "SELECT * FROM products WHERE id != %s ORDER BY RANDOM();"
        cursor.execute(query, (ID_PRODUCTO,))
        result = cursor.fetchall()

        data  = [dict(row) for row in result]

        cursor.close()
        connection.close()
        return  data
    except Exception as e:
        print(f"Error: {e}")
        return {'error': str(e)}

def getProduct(ID_PRODUCTO):
    try:
        connection  = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        query  = "SELECT * FROM products WHERE id = %s;"
        cursor.execute(query, (ID_PRODUCTO,))
        result = cursor.fetchall()

        data  = [dict(row) for row in result]

        cursor.close()
        connection.close()
        return  data
    except Exception as e:
        print(f"Error: {e}")
        return {'error': str(e)}
""" # Datos de ejemplo
data = [
    {"titulo": "Perfume 212", "precio": 10000, "rating": 4.5, "imagen": None, "categoria": "Belleza"},
    {"titulo": "Locion de hombre", "precio": 9000, "rating": 4.1, "imagen": None, "categoria": "Belleza"},
    {"titulo": "Smartphone Samsung Galaxy", "precio": 10000, "rating": 4.5, "imagen": None, "categoria": "Electrónica"},
    {"titulo": "Laptop HP 15 pulgadas", "precio": 1000, "rating": 4.5, "imagen": None, "categoria": "Electrónica"},
    {"titulo": "Laptop HP 15 pulgadas", "precio": 10000, "rating": 4.5, "imagen": None, "categoria": "Computo"},
    {"titulo": "Smartphone Samsung Galaxy", "precio": 10000, "rating": 4.7, "imagen": None, "categoria": "Electrónica"},
    {"titulo": "Audífonos inalámbricos", "precio": 2000, "rating": 4.2, "imagen": None, "categoria": "Accesorios"},
    {"titulo": "Smart TV LG 55 pulgadas", "precio": 15000, "rating": 4.8, "imagen": None, "categoria": "Electrónica"},
    {"titulo": "Mouse inalámbrico", "precio": 500, "rating": 4.0, "imagen": None, "categoria": "Accesorios"},
    {"titulo": "Lavadora de 20 Kg", "precio": 9500, "rating": 4.8, "imagen": None, "categoria": "Electrónica"},
] 
data = getData(1)
# Convertir los datos en un DataFrame
df = pd.DataFrame(data)

# Preprocesar los títulos con TF-IDF
tfidf = TfidfVectorizer(max_features=10)
titulo_tfidf = tfidf.fit_transform(df['name']).toarray()

# Normalizar precio y rating
scaler = MinMaxScaler()
scaled_features = scaler.fit_transform(df[['price', 'rating']])

# Codificar la categoría
label_encoder = LabelEncoder()
categoria_encoded = label_encoder.fit_transform(df['category']).reshape(-1, 1)

# Combinar todas las características
features = np.hstack([titulo_tfidf, scaled_features, categoria_encoded])

# Crear modelo k-NN
knn = NearestNeighbors(n_neighbors=3, metric='euclidean')
knn.fit(features)

# Encontrar productos similares al primero
distances, indices = knn.kneighbors([features[0]])

# Mostrar resultados
print("Producto inicial:", df.iloc[0]['name'])
print("Productos similares:")
for idx in indices[0][1:]:
    print(f"- {df.iloc[idx]['name']} (Distancia: {distances[0][list(indices[0]).index(idx)]:.2f})") """



def useKnn(ID_PRODUCTO):
    # Obtener los datos de la base de datos
    data = getProducts(ID_PRODUCTO)

    # Obtener el producto inicial
    new_element = getProduct(ID_PRODUCTO)[0]  # Obtener el primer diccionario de la lista

    # Agregar el nuevo elemento al inicio de los datos
    data.insert(0, new_element)

    # Crear el DataFrame con las claves correctas como nombres de columnas
    df = pd.DataFrame(data)

    # Preprocesar los títulos con TF-IDF (asegúrate de que 'name' esté en los datos)
    tfidf = TfidfVectorizer(max_features=10)
    titulo_tfidf = tfidf.fit_transform(df['name']).toarray()

    # Normalizar precio y rating
    scaler = MinMaxScaler()
    scaled_features = scaler.fit_transform(df[['price', 'rating']])

    # Codificar la categoría
    label_encoder = LabelEncoder()
    categoria_encoded = label_encoder.fit_transform(df['category']).reshape(-1, 1)

    # Combinar todas las características
    features = np.hstack([titulo_tfidf, scaled_features, categoria_encoded])

    # Crear modelo k-NN
    knn = NearestNeighbors(n_neighbors=30, metric='euclidean')
    knn.fit(features)

    # Encontrar productos similares al primero
    distances, indices = knn.kneighbors([features[0]])

    # Construir los resultados con claves y valores
    similar_products = []
    for idx in indices[0][1:]:  # Saltar el primer elemento (producto inicial)
        product = df.iloc[idx].to_dict()  # Convertir la fila en un diccionario
        product['distance'] = distances[0][list(indices[0]).index(idx)]  # Agregar la distancia como clave
        similar_products.append(product)

    # Mostrar resultados
    print("Producto inicial:", df.iloc[0]['name'])
    print("Productos similares:")
    for product in similar_products:
        print(f"- {product['name']} (Distancia: {product['distance']:.2f})")

    # Devolver el producto inicial y los productos similares
    return similar_products
