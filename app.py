from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensagem": "Bem-vindo a API FastOrder!"})

@app.route('/api/status')
def status():
    return jsonify({"status": "operacional", "servico": "FastOrder-Web"})

# =====================================================
# MISSÃO 5.1
@app.route('/api/soma')
def soma():
    try:
        a = request.args.get('a', default=0, type=float)
        b = request.args.get('b', default=0, type=float)

        resultado = a - b

        return jsonify({"resultado": resultado})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)