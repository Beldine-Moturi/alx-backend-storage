#!/usr/bin/env python3
"""
Defines a function that updates a document
in a collection"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
