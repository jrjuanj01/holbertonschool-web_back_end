#!/usr/bin/env python3
"""Module that contains an update school doc function"""


def update_topics(mongo_collection, name, topics):
    """Update Function"""
    
    mongo_collection.updateMany({'name': name}, {'$set': {"topics": topics}})
