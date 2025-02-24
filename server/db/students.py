from .utils import serialize_item, serialize_items
from .db import get_db

NAME = "name"
EMAIL = "email"
SENIORITY = "seniority"


def _get_student_collection():
    db = get_db()
    return db["students"]


def get_students(name: str = None, seniority: str = None):

    query = {}
    if name is not None:
        query[NAME] = {"$regex": name}
    if seniority is not None:
        query[SENIORITY] = seniority

    students = _get_student_collection().find(query)
    return serialize_items(list(students))


def create_student(name: str, email: str, seniority: str):
    student = {NAME: name, EMAIL: email, SENIORITY: seniority}
    result = _get_student_collection().insert_one(student)
    return result.inserted_id


def update_student(lookupemail: str, name: str, email: str, seniority: str):
    student_record = get_student_by_email(lookupemail)

    if student_record is None:
        return None

    new_data = {NAME: name, EMAIL: email, SENIORITY: seniority}
    result = _get_student_collection().update_one(
        {EMAIL: lookupemail}, {"$set": new_data}
    )

    return result


def delete_student(email: str):
    result = _get_student_collection().delete_one({EMAIL: email})
    return result.deleted_count


def get_student_by_email(email: str):
    student = _get_student_collection().find_one({EMAIL: email})
    return serialize_item(student)
