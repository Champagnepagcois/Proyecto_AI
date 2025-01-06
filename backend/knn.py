import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.neighbors import NearestNeighbors

# Datos de ejemplo
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

# Convertir los datos en un DataFrame
df = pd.DataFrame(data)

# Preprocesar los títulos con TF-IDF
tfidf = TfidfVectorizer(max_features=10)
titulo_tfidf = tfidf.fit_transform(df['titulo']).toarray()

# Normalizar precio y rating
scaler = MinMaxScaler()
scaled_features = scaler.fit_transform(df[['precio', 'rating']])

# Codificar la categoría
label_encoder = LabelEncoder()
categoria_encoded = label_encoder.fit_transform(df['categoria']).reshape(-1, 1)

# Combinar todas las características
features = np.hstack([titulo_tfidf, scaled_features, categoria_encoded])

# Crear modelo k-NN
knn = NearestNeighbors(n_neighbors=3, metric='euclidean')
knn.fit(features)

# Encontrar productos similares al primero
distances, indices = knn.kneighbors([features[0]])

# Mostrar resultados
print("Producto inicial:", df.iloc[0]['titulo'])
print("Productos similares:")
for idx in indices[0][1:]:
    print(f"- {df.iloc[idx]['titulo']} (Distancia: {distances[0][list(indices[0]).index(idx)]:.2f})")
