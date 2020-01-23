from core.clean_data import CleanData
from core.predict_data import PredictData
from core.load_data import LoadData
from flask import Flask, jsonify, request

app = Flask(__name__)

loader = LoadData()
cleaner = CleanData()
model = loader.load_model_from_path('./models/rf_model.pkl')
predicter = PredictData(model)

@app.route("/", methods=['POST'])
def do_prediction():
    json = request.get_json()
    df = loader.json_to_df(json)
    df = cleaner.clear_question_marks(df)
    X = cleaner.drop_unused_columns(df)

    prediction = predicter.predict(X)
    return jsonify(prediction[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)