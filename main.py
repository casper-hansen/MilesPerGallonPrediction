from core.clean_data import CleanData
from core.predict_data import PredictData

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()