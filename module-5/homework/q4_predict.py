import pickle

from flask import Flask
from flask import request
from flask import jsonify


def load(filename: str):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)


dv = load('dv.bin')
model = load('model1.bin')

app = Flask('subscription')


@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    get_subscription = y_pred >= 0.5

    result = {
        'get_subscription_probability': float(y_pred),
        'get_subscription': bool(get_subscription)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)


# how to run
# pipenv run gunicorn --bind localhost:8888 q4_predict:app
