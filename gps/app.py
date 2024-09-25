from flask import Flask, render_template, request, jsonify
from tspa import obtenerruta
from coord import coord

app = Flask(__name__)

@app.route('/')
def index():
    ciudades = list(coord.keys())
    return render_template('index.html', ciudades=ciudades)

@app.route('/get_routes', methods=['POST'])
def get_routes():
    data = request.get_json()
    start = data['start']
    end = data['end']
    
    try:
        ruta, distancia = obtenerruta(start, end)
        coordenadas_ruta = [coord[ciudad] for ciudad in ruta]
        nodos_intermedios_encontrados = ruta[1:-1]  # Excluye el inicio y el final de la ruta
        
        return jsonify({
            'origen': start,
            'destino': end,
            'coordenadas_ruta': coordenadas_ruta,
            'nodos_intermedios_encontrados': nodos_intermedios,
            'distancia': distancia
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
