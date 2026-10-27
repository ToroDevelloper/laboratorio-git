import os
import configcatclient
from flask import Flask, jsonify, request
from index import calculator

app = Flask(__name__)
calc = calculator()

# Inicializar cliente de ConfigCat
CONFIGCAT_KEY = os.environ.get("CONFIGCAT_SDK_KEY", "")
configcat_client = None

if CONFIGCAT_KEY:
    try:
        configcat_client = configcatclient.get(
            CONFIGCAT_KEY,
            options=configcatclient.ConfigCatOptions(
                polling_mode=configcatclient.PollingMode.auto_poll(poll_interval_seconds=5)
            ),
        )
    except Exception as e:
        print(f"Error inicializando ConfigCat: {e}")


def is_feature_enabled(key: str, default: bool = False) -> bool:
    if configcat_client:
        try:
            return configcat_client.get_value(key, default)
        except Exception as e:
            print(f"Error consultando toggle {key}: {e}")
            return default
    return default


@app.route("/")
def home():
    is_mult_on = is_feature_enabled("multiplication_enabled", False)
    return jsonify(
        {
            "name": "Laboratorio CI/CD - Calculadora API",
            "status": "running",
            "features": {"multiplication_enabled": is_mult_on},
            "endpoints": ["/healthz", "/sum", "/resta", "/multiplicacion"],
        }
    )


@app.route("/healthz")
def health_check():
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
    # Evaluación del Feature Toggle
    if not is_feature_enabled("multiplication_enabled", False):
        return (
            jsonify(
                {
                    "error": "Funcionalidad deshabilitada",
                    "message": "La operacion de multiplicacion se encuentra apagada por Feature Flag en ConfigCat.",
                    "feature_flag": "multiplication_enabled",
                    "status": "disabled",
                }
            ),
            403,
        )

    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify(
        {"operation": "multiplicacion", "a": a, "b": b, "result": calc.multiplicacion(a, b)}
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
