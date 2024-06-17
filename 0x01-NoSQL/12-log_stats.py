#!/usr/bin/env python3
"""
Provides stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def log_stats():
    """
    Prints statistics about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
