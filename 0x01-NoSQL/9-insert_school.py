#!/usr/bin/env python3
"""
Module for list_all documents in a collection
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    List all documents in a collection.
    """
    a = mongo_collection.insert_one(kwargs)
    return a.inserted_id
