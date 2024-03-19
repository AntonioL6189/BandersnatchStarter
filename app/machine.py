import datetime
import joblib
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier


class Machine:
    def __init__(self, df):
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)

    def __call__(self, pred_basis: DataFrame):
        predictions, *_ = self.model.predict(pred_basis)
        probability, *_ = self.model.predict_proba(pred_basis)
        return predictions, max(probability)

    def save(self, filepath):
        joblib.dump(self.model, filepath)

    @staticmethod
    def open(filepath):
        return joblib.load(filepath)

    def info(self):
        return f"basemodel:{self.name} <br> timestamp:{datetime.datetime.now()}"

