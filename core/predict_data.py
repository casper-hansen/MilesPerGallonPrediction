from sklearn.metrics import r2_score

class PredictData():
    def __init__(self, model = None):
        self.model = model
        self.pred = []
        self.score = None

    def predict(self, X_test, model = None):
        if model != None:
            self.pred = model.predict(X_test)
        else:
            self.pred = self.model.predict(X_test)
        
        return self.pred

    def score_r2(self, y_test):
        self.score = r2_score(y_test, self.pred)
        return self.score