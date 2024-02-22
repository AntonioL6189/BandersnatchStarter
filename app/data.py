from os import getenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient
from dotenv import load_dotenv
from certifi import where


class Database:
    load_dotenv()
    database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["Database"]

    def __init__(self, collection: str):
        self.collection = self.database[collection]

    def seed(self, amount=1000) -> bool:
        records = [Monster().to_dict() for i in range(amount)]
        return self.collection.insert_many(records).acknowledged

    def reset(self) -> bool:
        return self.collection.delete_many(filter={}).acknowledged

    def count(self) -> int:
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        return DataFrame(list(self.collection.find({}, {"_id": False})))

    def html_table(self) -> str:
        count = self.count()
        if count > 0:
            return self.dataframe().to_html()
        else:
            return "None"


if __name__ == '__main__':
    db = Database("Collection")
    db.seed()
    print("Collections created:", db.count())
