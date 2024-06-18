#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """

from pymongo import MongoClient


def count_documents(collection):
    return collection.count_documents({})


def count_method_documents(collection, method):
    return collection.count_documents({"method": method})


def count_status_check_documents(collection):
    return collection.count_documents({"method": "GET", "path": "/status"})


def get_top_ips(collection):
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    return list(collection.aggregate(pipeline))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = count_documents(collection)
    print(f"{total_logs} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = count_method_documents(collection, method)
        print(f"    method {method}: {count}")

    status_check_count = count_status_check_documents(collection)
    print(f"{status_check_count} status check")

    print("IPs:")
    top_ips = get_top_ips(collection)
    for ip_info in top_ips:
        ip = ip_info['_id']
        count = ip_info['count']
        print(f"    {ip}: {count}")
