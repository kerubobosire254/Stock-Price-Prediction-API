
from flask import Flask, request, jsonify
import numpy as np
import joblib
from tensorflow.keras.models import load_model

app = Flask(__name__)

# LOAD MODEL + SCALER
model = load_model("model.h5", compile=False)

scaler = joblib.load("scaler.pkl")

# must match training window size
WINDOW_SIZE = 60

# ROUTES
# prediction

@app.route("/")
def home():
    return "LSTM API is running 🚀"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        prices = np.array(data["prices"]).reshape(-1, 1)

        # give model enough history
        if len(prices) < WINDOW_SIZE:
            return jsonify({
                "error": f"Need at least {WINDOW_SIZE} values"
            })

        # converts to real prices
        scaled = scaler.transform(prices)

        # LSTM expects(samples, time_steps, features) 
        X_input = scaled[-WINDOW_SIZE:].reshape(1, WINDOW_SIZE, 1)

        # predict
        pred_scaled = model.predict(X_input)

        # inverse transform
        prediction = scaler.inverse_transform(pred_scaled)

        return jsonify({
            "prediction": float(prediction[0][0])
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

# RUN SERVER
if __name__ == "__main__":
    # FIX: prevents Jupyter / auto-reloader crash
    app.run(debug=True, use_reloader=False)