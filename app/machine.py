import joblib
from sklearn.ensemble import RandomForestClassifier
from pymongo import MongoClient


class Machine:
    def __init__(self, collection: str):
        client = MongoClient('localhost', 27017)
        self.database = client['Database']
        self.collection = self.database[collection]
        self.model = RandomForestClassifier()

    def __call__(self, feature_data):
        predictions = self.model.predict(feature_data)
        return predictions

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train)

    def predict(self, feature_data):
        predictions = self.model.predict(feature_data)
        return predictions

    def save(self, filepath):
        joblib.dump(self.model, filepath)

    @staticmethod
    def load(filepath):
        return joblib.load(filepath)

    def info(self):
        print("Model Information:")
        print(self.model)
