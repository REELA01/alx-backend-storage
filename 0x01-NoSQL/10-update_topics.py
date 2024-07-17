#!/usr/bin/env python3
"""change the school topic"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """update how  many rows"""
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
