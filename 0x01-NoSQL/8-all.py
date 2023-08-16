#!/user/bin/env python3
"""
Module for list_all documents in a collection
"""
from pymongo import MongoClienit
import pymongo


def list_all(mongo_collection):
    """
    List all documents in a collection.
    """
    a = mongo_collection.find({})
    if isinstance(a, pymongo.cursor.Cursor):
        return []
    else:
        return a
