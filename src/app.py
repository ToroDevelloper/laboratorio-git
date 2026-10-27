import os
from flask import Flask, jsonify, request
from index import calculator

app = Flask(__name__)
calc = calculator()


@app.route("/")
def home():
    return jsonify(
        {
            "name": "Laboratorio CI/CD - Calculadora API",
            "status": "running",
            "endpoints": ["/healthz", "/sum", "/resta", "/multiplicacion"],
        }
    )


@app.route("/healthz")
def health_check():
    # Endpoint de verificación de salud para Render
    return jsonify({"status": "healthy"}), 200


@app.route("/sum")
def do_sum():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"operation": "sum", "a": a, "b": b, "result": calc.sum(a, b)})


@app.route("/resta")
def do_resta():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"operation": "resta", "a": a, "b": b, "result": calc.resta(a, b)})


@app.route("/multiplicacion")
def do_multiplicacion():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify(
        {"operation": "multiplicacion", "a": a, "b": b, "result": calc.multiplicacion(a, b)}
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
