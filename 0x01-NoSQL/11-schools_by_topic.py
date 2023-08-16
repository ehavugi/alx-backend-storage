#!/user/bin/env python3
"""
Module for list of schools having a specific topic documents in a collection
"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topics):
    """
    List all documents in a collection.
    """
    mongo_collection.find({"topics":topics})
