from core.clean_data import CleanData
from core.predict_data import PredictData
from core.load_data import LoadData
from flask import Flask

app = Flask(__name__)

loader = LoadData()
cleaner = CleanData()
predicter = PredictData()

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)