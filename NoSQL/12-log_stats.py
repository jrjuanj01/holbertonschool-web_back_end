#!/usr/bin/env python3
from pymongo import MongoClient


def log_stats():
    """
    Provides stats about Nginx logs stored in MongoDB.
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Get the total number of logs
    total_logs = nginx_collection.count_documents({})

    # Count documents for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {
        method: nginx_collection.count_documents({"method": method})
        for method in methods
    }

    # Count the number of status checks (GET requests to /status)
    status_checks = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    # Print the results in the required format
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_checks} status check")


if __name__ == "__main__":
    log_stats()
