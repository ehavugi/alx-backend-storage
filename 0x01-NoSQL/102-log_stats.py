#!/usr/bin/env python3
""" 102 log stats. add most present IPs"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.logs.nginx
    count = 0
    methods = {}
    methodList = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    statusChecks = 0
    IPs = {}
    for i in school_collection.find():
        methodi = i.get("method")
        methods[methodi] = methods.get(methodi, 0) + 1
        ipi = i.get('ip')
        if ipi:
            IPs[ipi] = IPs.get(ipi, 0) + 1
        if i.get("path") == '/status':
            statusChecks += 1
        count += 1

    print("{} logs\nMethods:".format(count))
    for method in methodList:
        print("\tmethod {}: {}".format(method, methods.get(method, 0)))
    print("{} status check".format(statusChecks))
    count = 0
    print("IPs:")
    for ip in sorted(IPs, key=lambda key: IPs[key], reverse=True):
        if count < 10:
            print("\t{}: {}".format(ip, IPs.get(ip)))
        else:
            break
        count += 1
