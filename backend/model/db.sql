//------------productos:
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(400) NOT NULL,
  price FLOAT NOT NULL,
  rating FLOAT NOT NULL,
  image VARCHAR(400) NOT NULL,
  category VARCHAR(100) NOT NULL,
  date_upload DATE DEFAULT CURRENT_DATE NOT NULL,
  url VARCHAR(400) NOT NULL,
  details VARCHAR(400),
  quantity INTEGER
);



INSERT INTO products (name, price, rating, image, category, url)
VALUES (
    'AirPure Coca-Cola, CC-3D-V-V-405, Aromatizante Ventila 3D Aroma Vainilla, 13g',
    99,
    5,
    'https://images-na.ssl-images-amazon.com/images/I/81l9C8t37tL._AC_UL600_SR600,400_.jpg',
    'Automotriz y Motocicletas',
    'https://www.amazon.com.mx/Alfombrillas-furgoneta-protecci%C3%B3n-revestimientos-resistentes/dp/B088MN8J9Y/ref=zg_bsms_g_automotive_d_sccl_2/136-0941293-3600164?psc=1'
),
(
    'Cámara de Seguridad Exterior WiFi, Mini PTZ Cámara Inalámbrica Exterior Visión Nocturna, Audio Bidireccional, Detección de Movimiento',
    828,
    5,
    'https://m.media-amazon.com/images/I/51N+NlXV3lL._AC_UL320_.jpg',
    'Camaras',
    'https://www.amazon.com.mx/EASYTAO-2PCS-Inal%C3%A1mbrica-Bidireccional-MovimientY3_QTL8uvr7LAOEdSxAWzHEKRXnE1erDYQWMMzCSx3NAhjVecLo3pz3vAftDSrU.BLK1jV-PNDHcOOavoD3m-G5CbVkU4zjBabMUJvflCnU&dib_tag=se&keywords=camaras&qid=1734626245&sr=8-1&ufe=app_do%3Aamzn1.fos.de93fa6a-174c-4df7-be7c-5bc8e9c5a71b'
);

'AirPure Coca-Cola, CC-3D-V-V-405, Aromatizante Ventila 3D Aroma Vainilla, 13g'                                                          ,     99 ,      5 , 'https://images-na.ssl-images-amazon.com/images/I/81l9C8t37tL._AC_UL600_SR600,400_.jpg'  , 'Automotriz y Motocicletas' , 'https://www.amazon.com.mx/Alfombrillas-furgoneta-protecci%C3%B3n-revestimientos-resistentes/dp/B088MN8J9Y/ref=zg_bsms_g_automotive_d_sccl_2/136-0941293-3600164?psc=1'                                                                                                                                   
'Cámara de Seguridad Exterior WiFi, Mini PTZ Cámara Inalámbrica Exterior Visión Nocturna, Audio Bidireccional, Detección de Movimiento'  ,    828 ,      5 , 'https://m.media-amazon.com/images/I/51N+NlXV3lL._AC_UL320_.jpg'                         , 'Camaras'                   , 'https://www.amazon.com.mx/EASYTAO-2PCS-Inal%C3%A1mbrica-Bidireccional-MovimientY3_QTL8uvr7LAOEdSxAWzHEKRXnE1erDYQWMMzCSx3NAhjVecLo3pz3vAftDSrU.BLK1jV-PNDHcOOavoD3m-G5CbVkU4zjBabMUJvflCnU&dib_tag=se&keywords=camaras&qid=1734626245&sr=8-1&ufe=app_do%3Aamzn1.fos.de93fa6a-174c-4df7-be7c-5bc8e9c5a71b'



//------------------Productos banner

CREATE TABLE productBanner (
  id SERIAL PRIMARY KEY,
  image VARCHAR (400) NOT NULL,
  buttonText VARCHAR(50) DEFAULT 'Comprar ahora' NOT NULL,
  product VARCHAR(400) NOT NULL,
  description VARCHAR(400) ,
  smallText VARCHAR(55),
  midText VARCHAR(55),
  largeText1 VARCHAR(55) DEFAULT 'Promociones enero' NOT NULL,
  largeText2 VARCHAR(55),
  discount VARCHAR(255) ,
  saleTime VARCHAR(255) ,
  category VARCHAR(100) NOT NULL,
  url VARCHAR(400) NOT NULL
);



INSERT INTO productBanner (product, smallText,discount, image, category, url,description)
VALUES 
(
    '1 Hora Audifonos Inalambricos Diadema, Headphones con 100Hrs de Reproducción y 3 EQ Modos Musical, Plegables y Giratorios Bluetooth 5.3 Auriculares, Compatible con Teléfono/TV/PC',
    359,
    '15%',
    'https://cdn.sanity.io/images/hon77rsr/production/a64b345016e96adfb8849af5521c8e0ecfe8f027-555x555.webp',
    'Audio',
    'https://www.amazon.com.mx/Hora-Inalambricos-Headphones-Reproducci%C3%B3n-Auriculares/dp/B0D9BJM19G/ref=sr_1_11?__mk_es_M',
    '1 Hora Audifonos Inalambricos Diadema, Headphones con 100Hrs de Reproducción y 3 EQ Modos Musical, Plegables y Giratorios Bluetooth 5.3 Auriculares, Compatible con Teléfono/TV/PC'

),
(
    'STF Audífonos De Diadema Inalámbricos Aurum, Conexión 5.0, Micrófono Incorporado para Llamadas, Conexión De Cable 3.5 mm, Tiempo De Uso De hasta 10 Horas, Alcance Inalámbrico De 10 Metros (Gris)',
    399,
    '5%',
    'https://cdn.sanity.io/images/hon77rsr/production/a099db30fab841ce69c573f7409251824748e490-600x600.webp',
    'Audio',
    'https://www.amazon.com.mx/STF-Aud%C3%ADfonos-Inal%C3%A1mbricos-Incorporado-Inal%C3%A1mbrico/dp/B09NMKZGXB/ref=ci_mcx_mr_',
    'STF Audífonos De Diadema Inalámbricos Aurum, Conexión 5.0, Micrófono Incorporado para Llamadas, Conexión De Cable 3.5 mm, Tiempo De Uso De hasta 10 Horas, Alcance Inalámbrico De 10 Metros (Gris)'

),
(
    '1 Hora Bocina Bluetooth 10W, Barra de Sonido con 2400mAh Batería, Soundbar para PC TV, RGB Altavoces Inalámbricos Soporte 3.5mm AUX/TF/USB/Bluetooth para Interior, Hogar y Fiesta',
    339.99,
    '10%',
    'https://cdn.sanity.io/images/hon77rsr/production/9fbb62343426e1f157144f26d9b59be1629ef7c1-600x600.webp',
    'Audio',
    'https://www.amazon.com.mx/Hora-Bluetooth-Altavoces-Inal%C3%A1mbricos-Interior/dp/B0BTD4G6BH/ref=sr_1_9?__mk_es_MX=%C3%85',
    '1 Hora Bocina Bluetooth 10W, Barra de Sonido con 2400mAh Batería, Soundbar para PC TV, RGB Altavoces Inalámbricos Soporte 3.5mm AUX/TF/USB/Bluetooth para Interior, Hogar y Fiesta'

);




'1 Hora Audifonos Inalambricos Diadema, Headphones con 100Hrs de Reproducción y 3 EQ Modos Musical, Plegables y Giratorios Bluetooth 5.3 Auriculares, Compatible con Teléfono/TV/PC'                 ,    359 ,      4.8 , 'https://cdn.sanity.io/images/hon77rsr/production/a64b345016e96adfb8849af5521c8e0ecfe8f027-555x555.webp' , 'Audio', 'https://www.amazon.com.mx/Hora-Inalambricos-Headphones-Reproducci%C3%B3n-Auriculares/dp/B0D9BJM19G/ref=sr_1_11?__mk_es_M'
'STF Audífonos De Diadema Inalámbricos Aurum, Conexión 5.0, Micrófono Incorporado para Llamadas, Conexión De Cable 3.5 mm, Tiempo De Uso De hasta 10 Horas, Alcance Inalámbrico De 10 Metros (Gris)' ,    399 ,      4.7 , 'https://cdn.sanity.io/images/hon77rsr/production/a099db30fab841ce69c573f7409251824748e490-600x600.webp' , 'Audio', 'https://www.amazon.com.mx/STF-Aud%C3%ADfonos-Inal%C3%A1mbricos-Incorporado-Inal%C3%A1mbrico/dp/B09NMKZGXB/ref=ci_mcx_mr_'  
'1 Hora Bocina Bluetooth 10W, Barra de Sonido con 2400mAh Batería, Soundbar para PC TV, RGB Altavoces Inalámbricos Soporte 3.5mm AUX/TF/USB/Bluetooth para Interior, Hogar y Fiesta'                 , 339.99 ,      4.9 , 'https://cdn.sanity.io/images/hon77rsr/production/9fbb62343426e1f157144f26d9b59be1629ef7c1-600x600.webp' , 'Audio', 'https://www.amazon.com.mx/Hora-Bluetooth-Altavoces-Inal%C3%A1mbricos-Interior/dp/B0BTD4G6BH/ref=sr_1_9?__mk_es_MX=%C3%85'
