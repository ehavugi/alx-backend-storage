#!/usr/bin/env python3
"""
Module for list_all documents in a collection
"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    List all documents in a collection.
    """
    mongo_collection.update_many({"name": name}, topics)
