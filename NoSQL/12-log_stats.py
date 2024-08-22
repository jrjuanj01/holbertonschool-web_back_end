#!/usr/bin/env python3
"""Module with a stats function"""
from pymongo import MongoClient


def log_stats():
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    # Access the 'logs' database and the 'nginx' collection
    nginx_collection = client.logs.nginx

    # Get the total number of logs
    total_logs = nginx_collection.count_documents({})

    # Count documents for each HTTP method
    method_counts = {
        "GET": nginx_collection.count_documents({"method": "GET"}),
        "POST": nginx_collection.count_documents({"method": "POST"}),
        "PUT": nginx_collection.count_documents({"method": "PUT"}),
        "PATCH": nginx_collection.count_documents({"method": "PATCH"}),
        "DELETE": nginx_collection.count_documents({"method": "DELETE"}),
    }

    # Count the number of status checks (GET requests to /status)
    status_checks = nginx_collection.count_documents({"method": "GET", "path": "/status"})

    # Print the results
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_checks} status check")

if __name__ == "__main__":
    log_stats()

