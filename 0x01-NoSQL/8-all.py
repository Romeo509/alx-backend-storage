#!/usr/bin/env python3
"""
This module provides a function to list all documents in a MongoDB collection.
"""

def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of all documents in the collection. Returns an empty list if no document in the collection.
    """
    return list(mongo_collection.find())
