#!/usr/bin/env python3
""" 11-main """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.logs.nginx
    count = 0
    methods = {}
    methodList = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    statusChecks = 0
    for i in school_collection.find():
        methodi = i.get("method")
        methods[methodi] = methods.get(methodi, 0) + 1
        if i.get("path") == '/status':
            statusChecks += 1
        count += 1

    print("{} logs\nMethods:".format(count))
    for method in methodList:
        print("    method {}: {}".format(method, methods.get(method, 0)))
    print("{} status check".format(statusChecks))
