from flask import Flask, render_template, request, jsonify
from ruleta import apostar, vermells, negres

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/girar', methods=['POST'])
def girar():
    data = request.json
    tipo_apuesta = data.get('tipo_apuesta')
    valor_apuesta = data.get('valor_apuesta')
    ficha = data.get('ficha')
    numero_tirada = data.get('numero_tirada', 1)  # Obtenir el número de tirada
    
    # Convertir valor_apuesta a número si és tipus "numero"
    if tipo_apuesta == "numero":
        valor_apuesta = int(valor_apuesta)
    
    # Processar l'aposta passant el número de tirada
    numero, color, ganancia = apostar(tipo_apuesta, valor_apuesta, numero_tirada)
    
    # Calcular guany en euros
    ganancia_euros = ficha * ganancia if ganancia > 0 else 0
    
    return jsonify({
        'numero': numero,
        'color': color,
        'ganancia': ganancia,
        'ganancia_euros': ganancia_euros
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
