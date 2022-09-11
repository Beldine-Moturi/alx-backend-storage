#!/usr/bin/env python3
"""Pymongo practice"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx

    # n = logs.count_documents({})
    print(f'{logs.count_documents({})} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = logs.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check = logs.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_check} status check')
