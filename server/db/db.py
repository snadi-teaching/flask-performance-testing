import pymongo

# Global variable to hold the database client instance
db_client = None
db_name = "school_db"


def init_db(app):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    app.config["DB_CLIENT"] = client
    app.config["DB_NAME"] = db_name
    global db_client
    db_client = client


def get_db():
    if db_client is None:
        raise Exception(
            "Database client is not initialized. Call init_db(uri, db_name) first."
        )
    return db_client[db_name]


def get_collection(collection_name):
    db = get_db()
    return db[collection_name]
