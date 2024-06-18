#!/usr/bin/env python3
""" MongoDB Operations using Python and pymongo """

from pymongo import MongoClient

def display_nginx_stats(nginx_collection):
    """Displays various statistics from Nginx logs."""
    total_logs = nginx_collection.count_documents({})
    print('{} logs'.format(total_logs))
    
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print('\tmethod {}: {}'.format(method, count))
    
    status_check_count = nginx_collection.count_documents({
        'method': 'GET', 'path': '/status'
    })
    print('{} status check'.format(status_check_count))

def display_top_ips(nginx_collection):
    """Shows the top 10 IPs found in Nginx logs."""
    print('IPs:')
    top_ips = nginx_collection.aggregate([
        {'$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}},
        {'$sort': {'totalRequests': -1}},
        {'$limit': 10}
    ])
    for ip in top_ips:
        print('\t{}: {}'.format(ip['_id'], ip['totalRequests']))

def main():
    """Connects to MongoDB and displays Nginx log stats."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    display_nginx_stats(nginx_collection)
    display_top_ips(nginx_collection)

if __name__ == '__main__':
    main()
