#!/user/bin/env python3
"""
Module for list_all documents in a collection
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    List all documents in a collection.
    """
    print("kwargs", kwargs)
    a = mongo_collection.insert_one(kwargs)
    print("a", a, dir(a))
    return a.inserted_id
