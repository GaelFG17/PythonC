coord = {
    "Baja California": [30.033892, -115.142511],
    "Baja California Sur": [24.14437, -110.3005],
    "Sonora": [29.1026, -110.97732],
    "Chihuahua": [28.63528, -106.08889],
    "Sinaloa": [23.2329, -106.4062],
    "Durango": [24.02032, -104.65756],
    "Coahuila": [25.42321, -101.0053],
    "Nayarit": [22.0000001, -105.0000001],
    "Zacatecas": [22.76843, -102.58141],
    "Nuevo León": [25.67507, -100.31847],
    "Tamaulipas": [22.36094, -97.89997],
    "San Luis Potosí": [22.14982, -100.97916],
    "Aguascalientes": [21.88234, -102.28259],
    "Jalisco": [20.66682, -103.39182],
    "Colima": [19.24997, -103.72714],
    "Michoacán": [19.70078, -101.18443],
    "Guanajuato": [20.52353, -100.8157],
    "Querétaro": [20.58806, -100.38806],
    "Hidalgo": [20.11697, -98.73329],
    "Estado de México": [19.28786, -99.65324],
    "CDMX": [19.42847, -99.12766],
    "Morelos": [19.60492, -99.06064],
    "Guerrero": [16.79772, -99.38921],
    "Puebla": [19.03793, -98.20346],
    "Tlaxcala": [19.31905, -98.19982],
    "Veracruz": [19.31905, -98.19982],
    "Oaxaca": [16.75973, -93.11308],
    "Chiapas": [16.75973, -93.11308],
    "Tabasco": [17.98689, -92.93028],
    "Campeche": [17.98689, -92.93028],
    "Yucatán": [20.97537, -89.61696],
    "Quintana Roo": [18.51413, -88.30381] 
}

# Diccionario de colindaciones y distancias
colindaciones = {
    "Baja California": {
        "Sonora": 866,
        "Baja California Sur": 1467 
    },
    "Baja California Sur": {
        "Baja California": 1467  
    },
    "Sonora": {
        "Baja California": 864,
        "Chihuahua": 693,
        "Sinaloa": 701
    },
    "Chihuahua": {
        "Sonora": 666,
        "Sinaloa": 693,
        "Durango": 566,
        "Coahuila": 747
    },
    "Sinaloa": {
        "Chihuahua": 693,
        "Durango": 573,
        "Nayarit": 567
    },
    "Durango": {
        "Chihuahua": 566,
        "Coahuila": 551,
        "Nayarit": 493,
        "Zacatecas": 289,
        "Sinaloa": 573
    },
    "Coahuila": {
        "Chihuahua": 747,
        "Durango": 551,
        "Zacatecas": 550,
        "Nuevo León": 150,
        "San Luis Potosí": 689
    },
    "Nayarit": {
        "Sinaloa": 567,
        "Durango": 493,
        "Zacatecas": 250,
        "Jalisco": 220
    },
    "Zacatecas": {
        "Aguascalientes": 118,
        "Durango": 289,
        "Nayarit": 250,
        "Jalisco": 300,
        "Coahuila": 550,
        "San Luis Potosí": 200
    },
    "Nuevo León": {
        "Coahuila": 150,
        "Tamaulipas": 200,
        "San Luis Potosí": 300
    },
    "Tamaulipas": {
        "Nuevo León": 200,
        "San Luis Potosí": 300,
        "Veracruz": 350
    },
    "San Luis Potosí": {
        "Nuevo León": 300,
        "Coahuila": 689,
        "Zacatecas": 200,
        "Tamaulipas": 300,
        "Querétaro": 250,
        "Guanajuato": 270,
        "Hidalgo": 350
    },
    "Aguascalientes": {
        "Jalisco": 222,
        "Zacatecas": 118,
        "Guanajuato": 200
    },
    "Jalisco": {
        "Aguascalientes": 222,
        "Nayarit": 220,
        "Colima": 150,
        "Guanajuato": 250,
        "Zacatecas": 300,
        "Michoacán": 300
    },
    "Colima": {
        "Jalisco": 150,
        "Michoacán": 200
    },
    "Michoacán": {
        "Colima": 200,
        "Guanajuato": 300,
        "Querétaro": 300,
        "Estado de México": 250,
        "Guerrero": 200
    },
    "Guanajuato": {
        "Jalisco": 250,
        "Zacatecas": 250,
        "San Luis Potosí": 270,
        "Querétaro": 100,
        "Michoacán": 300
    },
    "Querétaro": {
        "San Luis Potosí": 250,
        "Guanajuato": 100,
        "Hidalgo": 150,
        "Estado de México": 150,
        "Michoacán": 300
    },
    "Hidalgo": {
        "Querétaro": 150,
        "San Luis Potosí": 350,
        "Estado de México": 120,
        "Tlaxcala": 160,
        "Veracruz": 300
    },
    "Estado de México": {
        "Querétaro": 150,
        "Hidalgo": 120,
        "Tlaxcala": 100,
        "Puebla": 150,
        "Morelos": 100,
        "CDMX": 50,
        "Michoacán": 250
    },
    "CDMX": {
        "Estado de México": 50,
        "Morelos": 50
    },
    "Morelos": {
        "CDMX": 50,
        "Estado de México": 100,
        "Puebla": 120,
        "Guerrero": 180
    },
    "Guerrero": {
        "Morelos": 180,
        "Estado de México": 250,
        "Michoacán": 200,
        "Puebla": 300,
        "Oaxaca": 350
    },
    "Puebla": {
        "Tlaxcala": 40,
        "Estado de México": 150,
        "Hidalgo": 200,
        "Veracruz": 250,
        "Morelos": 120,
        "Guerrero": 300,
        "Oaxaca": 350
    },
    "Tlaxcala": {
        "Puebla": 40,
        "Hidalgo": 160,
        "Estado de México": 100
    },
    "Veracruz": {
        "Puebla": 250,
        "Hidalgo": 300,
        "San Luis Potosí": 400,
        "Tabasco": 250,
        "Oaxaca": 350,
        "Chiapas": 500,
        "Tamaulipas": 350
    },
    "Oaxaca": {
        "Veracruz": 350,
        "Puebla": 350,
        "Guerrero": 350,
        "Chiapas": 220
    },
    "Chiapas": {
        "Veracruz": 500,
        "Oaxaca": 220,
        "Tabasco": 200
    },
    "Tabasco": {
        "Chiapas": 200,
        "Veracruz": 250,
        "Campeche": 150
    },
    "Campeche": {
        "Tabasco": 150,
        "Yucatán": 150,
        "Quintana Roo": 300
    },
    "Yucatán": {
        "Campeche": 150,
        "Quintana Roo": 300
    },
    "Quintana Roo": {
        "Yucatán": 300,
        "Campeche": 300
    }
}

